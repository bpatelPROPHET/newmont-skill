#!/usr/bin/env python3
"""Check a pptx against the Newmont brand rules: fonts, palette, effects, furniture, size, required text.
Usage: python check_deck.py deck.pptx [--deck-name "Newmont – X"] [--content-slides 3,4,5] [--no-furniture-slides 1,6] [--expect-slides 6] [--required-text brief.txt]
Prints PASS/FAIL per rule; fix every FAIL before delivering. Needs python-pptx and lxml (both come with python-pptx)."""
import argparse, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PALETTE = set("0C2B82 071434 12A6E6 FCAF17 FFFFFF 00A9EC FFAB00 061641 010310 A6A6A6 BFBFBF 7F7F7F "
              "EDEDEE CEEEFB F2F2F2 DFDFDF D9D9D9 000000 E9F6FC F6FAFC".split())
BAD_GEOM = {"roundRect", "round1Rect", "round2SameRect", "round2DiagRect", "snipRoundRect"}


def norm(s):
    return re.sub(r"\s+", " ", (s or "").replace("–", "-").replace("—", "-").replace("\u2019", "'").replace("\u2018", "'")).strip().lower()


def ev(items, n=5):
    return "; ".join(items[:n]) + (" (+%d more)" % (len(items) - n) if len(items) > n else "") if items else ""


def loc(sl, sh, extra=""):
    return "slide %d '%s'%s" % (sl["index"], sh["name"], extra)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--out", default=None, help="optional JSON results file")
    ap.add_argument("--expect-slides", type=int)
    ap.add_argument("--deck-name")
    ap.add_argument("--required-text")
    ap.add_argument("--content-slides", default="")
    ap.add_argument("--no-furniture-slides", default="")
    a = ap.parse_args()
    res = []

    def add(text, passed, evidence):
        res.append({"text": text, "passed": bool(passed), "evidence": evidence})

    def finish():
        if a.out: json.dump(res, open(a.out, "w"), indent=1)
        for r in res:
            print(("PASS " if r["passed"] else "FAIL ") + r["text"] + "\n     " + r["evidence"][:400])

    if not os.path.exists(a.file):
        add("The pptx file exists and opens", False, "file not found: " + a.file)
        finish(); return
    try:
        import inspect_pptx
        d = inspect_pptx.inspect(a.file)
        add("The pptx file exists and opens", True, "%d slides found" % len(d["slides"]))
    except Exception as e:
        add("The pptx file exists and opens", False, "error: %r (check_deck.py needs inspect_pptx.py beside it; copy both from the skill's scripts folder)" % e)
        finish(); return
    slides = d["slides"]
    if a.expect_slides is not None:
        add("The deck has exactly %d slides" % a.expect_slides, len(slides) == a.expect_slides,
            "found %d slides" % len(slides))
    add("The slide size is 960 x 540 pt (13.333 x 7.5 in)",
        abs(d["slide_w_pt"] - 960) <= 1 and abs(d["slide_h_pt"] - 540) <= 1,
        "size is %s x %s pt" % (d["slide_w_pt"], d["slide_h_pt"]))

    bad = []
    for sl in slides:
        for sh in sl["shapes"]:
            for r in sh.get("runs", []):
                t = r["text"]
                if not t.strip() or t.strip() == "•":
                    continue
                if r["font"] is None:
                    bad.append("%s run %r has no latin typeface (inherits theme font, renders Calibri)" % (loc(sl, sh), t[:30]))
                elif r["font"] != "Open Sans":
                    bad.append("%s run %r uses %s" % (loc(sl, sh), t[:30], r["font"]))
    add("Every text run is set explicitly in Open Sans (no other or inherited font)", not bad, ev(bad) or "all runs Open Sans")

    bad = []
    def chk(c, where):
        if c and c not in ("inherited", "none", "gradient", "scheme", "picture") and c not in PALETTE:
            bad.append("%s colour %s" % (where, c))
        if c == "scheme":
            bad.append("%s uses a theme/scheme colour" % where)
    for sl in slides:
        if sl["background"]:
            chk(sl["background"], "slide %d background" % sl["index"])
        for sh in sl["shapes"]:
            chk(sh["fill"], loc(sl, sh, " fill"))
            chk(sh["line"]["color"], loc(sl, sh, " line"))
            for r in sh.get("runs", []):
                if r["text"].strip():
                    chk(r["color"], loc(sl, sh, " text %r" % r["text"][:20]))
    add("Every fill, line and text colour is from the Newmont palette", not bad, ev(bad) or "all colours in palette")

    bad = []
    for sl in slides:
        if sl["background_kind"] == "gradient":
            bad.append("slide %d background is a gradient" % sl["index"])
        for sh in sl["shapes"]:
            if sh["has_effects"]:
                bad.append(loc(sl, sh) + " has effectLst")
            if sh["has_p_style"]:
                bad.append(loc(sl, sh) + " has p:style (theme shadow/line refs)")
            if sh["fill"] == "gradient":
                bad.append(loc(sl, sh) + " has gradFill")
            if sh["geometry"] in BAD_GEOM:
                bad.append(loc(sl, sh) + " is %s" % sh["geometry"])
    add("No shape has effects, theme style references, gradients or rounded corners", not bad, ev(bad) or "flat")

    def parse(s):
        return [int(x) for x in re.findall(r"\d+", s)]
    byi = {s["index"]: s for s in slides}
    cs = parse(a.content_slides)
    if cs:
        bad = []
        for i in cs:
            sl = byi.get(i)
            if not sl:
                bad.append("slide %d missing" % i); continue
            f = sl["furniture"]; ft = norm(" ".join(f["footer_texts"])).upper()
            if not f["has_logo"]: bad.append("slide %d: no logo" % i)
            if "NEWMONT CORPORATION" not in ft: bad.append("slide %d: footer lacks NEWMONT CORPORATION (footer=%r)" % (i, ft[:60]))
            if a.deck_name and norm(a.deck_name).upper() not in ft:
                bad.append("slide %d: footer lacks deck name" % i)
            if not f["page_number"]: bad.append("slide %d: no page number" % i)
        add("Content slides %s each have the logo, a footer with NEWMONT CORPORATION%s, and a page number"
            % (a.content_slides, " and the deck name" if a.deck_name else ""), not bad, ev(bad) or "all present")
    nf = parse(a.no_furniture_slides)
    if nf:
        bad = []
        for i in nf:
            sl = byi.get(i)
            if sl and "NEWMONT CORPORATION" in norm(" ".join(sl["furniture"]["footer_texts"])).upper():
                bad.append("slide %d has a NEWMONT CORPORATION footer" % i)
        add("Slides %s have no NEWMONT CORPORATION footer" % a.no_furniture_slides, not bad, ev(bad) or "none present")

    if a.required_text:
        alltext = norm(" ".join(r["text"] for sl in slides for sh in sl["shapes"] for r in sh.get("runs", [])))
        # also join paragraph-split text without spaces issue: check both
        lines = [norm(l) for l in open(a.required_text, encoding="utf-8").read().splitlines() if l.strip()]
        miss = [l for l in lines if l not in alltext]
        add("Every required text line appears verbatim in the deck", not miss,
            ("missing %d of %d: " % (len(miss), len(lines)) + ev(miss)) if miss else "all %d lines found" % len(lines))
    finish()


if __name__ == "__main__":
    main()
