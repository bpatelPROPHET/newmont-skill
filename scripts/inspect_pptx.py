#!/usr/bin/env python3
"""Dump a JSON description of a pptx by walking raw XML. Usage: inspect_pptx.py file.pptx"""
import json, re, sys, zipfile
from lxml import etree

NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
A = "{%s}" % NS["a"]
P = "{%s}" % NS["p"]
EMU = 12700.0
SHAPE_TAGS = {P + "sp": "sp", P + "pic": "picture", P + "cxnSp": "connector",
              P + "graphicFrame": "graphicFrame", P + "grpSp": "group"}


def pt(v):
    return round(int(v) / EMU, 2)


def fill_of(sppr):
    if sppr is None:
        return "inherited"
    if sppr.find("a:noFill", NS) is not None:
        return "none"
    if sppr.find("a:gradFill", NS) is not None:
        return "gradient"
    sf = sppr.find("a:solidFill", NS)
    if sf is not None:
        c = sf.find("a:srgbClr", NS)
        if c is not None:
            return c.get("val").upper()
        return "scheme"
    if sppr.find("a:blipFill", NS) is not None:
        return "picture"
    return "inherited"


def line_of(sppr):
    ln = sppr.find("a:ln", NS) if sppr is not None else None
    if ln is None:
        return {"color": "inherited", "width_pt": None}
    w = pt(ln.get("w")) if ln.get("w") else None
    if ln.find("a:noFill", NS) is not None:
        return {"color": "none", "width_pt": w}
    c = ln.find("a:solidFill/a:srgbClr", NS)
    if c is not None:
        return {"color": c.get("val").upper(), "width_pt": w}
    if ln.find("a:solidFill", NS) is not None:
        return {"color": "scheme", "width_pt": w}
    return {"color": "inherited", "width_pt": w}


def runs_of(el, y):
    out = []
    for r in el.iter(A + "r"):
        rpr = r.find("a:rPr", NS)
        t = r.find("a:t", NS)
        d = {"text": t.text or "" if t is not None else "", "font": None, "size_pt": None,
             "bold": None, "italic": None, "color": None, "spc": None}
        if rpr is not None:
            lat = rpr.find("a:latin", NS)
            d["font"] = lat.get("typeface") if lat is not None else None
            d["size_pt"] = int(rpr.get("sz")) / 100 if rpr.get("sz") else None
            d["bold"] = rpr.get("b") in ("1", "true") if rpr.get("b") is not None else None
            d["italic"] = rpr.get("i") in ("1", "true") if rpr.get("i") is not None else None
            c = rpr.find("a:solidFill/a:srgbClr", NS)
            d["color"] = c.get("val").upper() if c is not None else None
            d["spc"] = int(rpr.get("spc")) if rpr.get("spc") is not None else None
        d["y_pt"] = y
        out.append(d)
    return out


def walk(tree, ox=0, oy=0, sx=1.0, sy=1.0):
    """Yield shape dicts, descending into groups (approximate absolute position)."""
    for el in tree:
        kind = SHAPE_TAGS.get(el.tag)
        if kind is None:
            continue
        nv = el.find(".//p:cNvPr", NS)
        name = nv.get("name") if nv is not None else ""
        if kind == "group":
            gp = el.find("p:grpSpPr", NS)
            xf = gp.find("a:xfrm", NS) if gp is not None else None
            if xf is not None:
                off, ext = xf.find("a:off", NS), xf.find("a:ext", NS)
                cho, che = xf.find("a:chOff", NS), xf.find("a:chExt", NS)
                gx, gy = int(off.get("x")), int(off.get("y"))
                gw, gh = int(ext.get("cx")), int(ext.get("cy"))
                cx0, cy0 = int(cho.get("x")), int(cho.get("y"))
                cw, ch = int(che.get("cx")) or 1, int(che.get("cy")) or 1
                nsx, nsy = gw / cw, gh / ch
                yield from walk(el, ox + (gx - cx0 * nsx) * sx, oy + (gy - cy0 * nsy) * sy, sx * nsx, sy * nsy)
            else:
                yield from walk(el, ox, oy, sx, sy)
            continue
        sppr = el.find("p:spPr", NS)
        xf = sppr.find("a:xfrm", NS) if sppr is not None else None
        if xf is None and kind == "graphicFrame":
            xf = el.find("p:xfrm", NS)
        x = y = w = h = None
        if xf is not None and xf.find("a:off", NS) is not None:
            off, ext = xf.find("a:off", NS), xf.find("a:ext", NS)
            x = pt(ox + int(off.get("x")) * sx); y = pt(oy + int(off.get("y")) * sy)
            w = pt(int(ext.get("cx")) * sx); h = pt(int(ext.get("cy")) * sy)
        geom = None
        if sppr is not None:
            pg = sppr.find("a:prstGeom", NS)
            if pg is not None:
                geom = pg.get("prst")
            elif sppr.find("a:custGeom", NS) is not None:
                geom = "freeform"
        is_tx = el.find("p:nvSpPr/p:cNvSpPr", NS)
        is_tx = is_tx is not None and is_tx.get("txBox") == "1"
        if kind == "picture":
            geom = "picture"
        elif kind == "connector":
            geom = geom or "connector"
        elif is_tx and geom in (None, "rect"):
            geom = "textbox"
        eff = sppr.find("a:effectLst", NS) if sppr is not None else None
        d = {"type": kind, "name": name, "geometry": geom, "textbox": is_tx,
             "x_pt": x, "y_pt": y, "w_pt": w, "h_pt": h,
             "fill": "none" if kind == "picture" else fill_of(sppr),
             "line": line_of(sppr),
             "has_effects": eff is not None and len(eff) > 0,
             "has_p_style": el.find("p:style", NS) is not None}
        tb = el.find("p:txBody", NS)
        if tb is not None:
            d["runs"] = runs_of(tb, y)
        elif kind == "graphicFrame":
            d["runs"] = runs_of(el, y)
        yield d


def inspect(path):
    z = zipfile.ZipFile(path)
    pres = etree.fromstring(z.read("ppt/presentation.xml"))
    sz = pres.find("p:sldSz", NS)
    names = sorted([n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)],
                   key=lambda n: int(re.findall(r"\d+", n)[-1]))
    # honour presentation order
    rels = etree.fromstring(z.read("ppt/_rels/presentation.xml.rels"))
    rid2t = {r.get("Id"): r.get("Target") for r in rels}
    order = []
    for sid in pres.findall("p:sldIdLst/p:sldId", NS):
        t = rid2t.get(sid.get("{%s}id" % NS["r"]))
        if t:
            order.append("ppt/" + t.lstrip("/").replace("ppt/", ""))
    names = order or names
    out = {"slide_w_pt": pt(sz.get("cx")), "slide_h_pt": pt(sz.get("cy")), "slides": []}
    for i, n in enumerate(names, 1):
        root = etree.fromstring(z.read(n))
        bg = None
        bgel = root.find("p:cSld/p:bg", NS)
        bg_kind = None
        if bgel is not None:
            c = bgel.find(".//a:solidFill/a:srgbClr", NS)
            if c is not None:
                bg = c.get("val").upper()
            elif bgel.find(".//a:gradFill", NS) is not None:
                bg_kind = "gradient"
        shapes = list(walk(root.find("p:cSld/p:spTree", NS)))
        logo = False
        for s in shapes:
            nm = (s["name"] or "").lower()
            if s["geometry"] == "freeform" and s["fill"] == "FCAF17" and s["w_pt"] is not None \
                    and 20 <= s["w_pt"] <= 40 and 30 <= s["y_pt"] <= 60:
                logo = True
            if "logo" in nm and s["type"] in ("picture", "sp", "group"):
                logo = True
        # group named logo
        for g in root.iter(P + "grpSp"):
            nv = g.find("p:nvGrpSpPr/p:cNvPr", NS)
            if nv is not None and "logo" in (nv.get("name") or "").lower():
                logo = True
        footer, pn = [], None
        for s in shapes:
            for r in s.get("runs", []):
                yy = r["y_pt"]
                if yy is None:
                    continue
                if r["size_pt"] is not None and r["size_pt"] <= 9 and yy > 500 and r["text"].strip():
                    footer.append(r["text"])
                if yy > 500 and re.fullmatch(r"\s*\d+\s*", r["text"] or ""):
                    pn = r["text"].strip()
        out["slides"].append({
            "index": i, "part": n, "background": bg, "background_kind": bg_kind,
            "has_picture": any(s["type"] == "picture" for s in shapes),
            "shapes": shapes,
            "furniture": {"has_logo": logo, "footer_texts": footer, "page_number": pn}})
    return out


if __name__ == "__main__":
    print(json.dumps(inspect(sys.argv[1]), indent=1))
