"""Build the Newmont quarterly financials executive summary template, v2 (2 content pages)."""
import os
import sys

sys.path.insert(0, '/Users/bpatel/dev/newmont-skill/scripts')
from newmont_kit import Deck, NAVY, SKY, MUTED, RULE_GREY, PP_ALIGN  # noqa: E402

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(OUT_DIR, 'newmont-quarterly-executive-summary.pptx')
DECK_NAME = 'Newmont – Q[X] 20XX Financial Results'

DELTAS = ['[+0.0%] vs Q[X-1]', '[+0.0%] vs prior year']
KPIS = [('GOLD PRODUCTION', '[0,000 koz]', DELTAS),
        ('ALL-IN SUSTAINING COST', '[$0,000/oz]', DELTAS),
        ('ADJUSTED EBITDA', '[$0.0B]', DELTAS),
        ('FREE CASH FLOW', '[$0.0B]', DELTAS)]
DRIVERS = (('Production:', '[One sentence on volumes and the sites that moved them.]'),
           ('Costs:', '[One sentence on AISC and the main cost drivers.]'),
           ('Cash and balance sheet:', '[One sentence on free cash flow, net debt and shareholder returns.]'))
GUIDANCE_HEADER = ('Metric', 'FY guidance', 'YTD')
GUIDANCE = (('Gold production', '[0,000–0,000 koz]', '[0,000 koz]'),
            ('AISC', '[$0,000–0,000/oz]', '[$0,000/oz]'),
            ('Sustaining capital', '[$0.0–0.0B]', '[$0.0B]'),
            ('Development capital', '[$0.0–0.0B]', '[$0.0B]'))
P = ('[0,000]', '[0,000]', '[0,000]', '[+0.0%]')
PS = ('[0.00]', '[0.00]', '[0.00]', '[+0.0%]')
TABLE_HEADER = ('USD millions unless stated', 'Q[X] 20XX', 'Q[X-1] 20XX', 'Q[X] 20XX-1', 'Δ vs Q[X-1]')
TABLE_GROUPS = [
    ('OPERATING', [('Attributable gold production (koz)',) + P,
                   ('All-in sustaining cost ($/oz)',) + P,
                   ('Realized gold price ($/oz)',) + P]),
    ('FINANCIAL', [('Revenue',) + P,
                   ('Adjusted EBITDA',) + P,
                   ('Adjusted net income',) + P,
                   ('Adjusted net income per share ($)',) + PS,
                   ('Free cash flow',) + P]),
    ('BALANCE SHEET AND RETURNS', [('Net debt',) + P,
                                   ('Dividend declared per share ($)',) + PS])]


def eyebrow(d, s, x, glyph_top, label, w=400):
    d.text(s, x, glyph_top, w, [label], 10.5, SKY, bold=True, em=0.015, caps=True)


def drivers(d, s):
    eyebrow(d, s, 36, 216, 'WHAT DROVE THE QUARTER')
    paras, opts = [], []
    for k, (head, body) in enumerate(DRIVERS):
        paras += [[(head, True, False)], [(body, False, False)]]
        opts += [{'space_before': 12 if k else 0}, {}]
    d.text(s, 36, 239.5, 420, paras, 12, NAVY, em=0.008, pitch=18, h=150, opts=opts)


def guidance(d, s):
    eyebrow(d, s, 487.5, 216, 'AGAINST FULL-YEAR GUIDANCE')
    cols, x1, y = (487.5, 700, 815), 928, 236
    edges = cols + (x1,)
    for r, cells in enumerate((GUIDANCE_HEADER,) + GUIDANCE):
        bold, hgt = (True, 21.6) if r == 0 else (False, 24)
        for i, c in enumerate(cells):
            d.text(s, cols[i] + 7, y + 6, edges[i + 1] - cols[i] - 14, [c], 12, NAVY, bold=bold, em=0.004,
                   pitch=14.3, h=16, align=PP_ALIGN.RIGHT if i else None)
        y += hgt
        d.line(s, cols[0], y, x1, y, *((NAVY, 1.5) if bold else (RULE_GREY, 0.75)))


def outlook_and_note(d, s):
    d.line(s, 36, 392, 928, 392, NAVY, 0.5)
    eyebrow(d, s, 36, 404, 'OUTLOOK AND DECISIONS')
    d.text(s, 36, 421, 892, ['[One or two sentences on the full-year outlook and the decisions the '
                             'executive team is asked to take.]'], 12, NAVY, em=0.008, pitch=18, h=20)
    d.text(s, 35.8, 448.7, 300, ['Note'], 10, MUTED, bold=True)
    d.text(s, 35.8, 460.8, 660, ['[Adjusted EBITDA, free cash flow and AISC are non-GAAP measures; '
                                 'see the reconciliation in the appendix.]'],
           10, MUTED, em=0.013, pitch=12, h=40)


def page_summary(d):
    # Placeholder kept to one line: a two-line title collides with the eyebrow at 83pt.
    s = d.blank('[Key message, e.g. Record free cash flow on higher gold prices]')
    eyebrow(d, s, 36, 83, 'EXECUTIVE SUMMARY | Q[X] 20XX')
    d.kpi_tiles(s, KPIS, y=100)
    drivers(d, s)
    guidance(d, s)
    outlook_and_note(d, s)


def page_table(d):
    # Placeholder kept to one line: a two-line title collides with the subtitle at 61.6pt.
    s = d.blank('[What moved and why, e.g. Costs fell while production held]')
    d.text(s, 36, 61.6, 700, ['Q[X] 20XX compared with Q[X-1] 20XX and Q[X] 20XX-1'], 16, NAVY, bold=True, em=0.02)
    end = d.fin_table(s, TABLE_HEADER, TABLE_GROUPS, y=100, col_w=[105, 105, 105, 105], row_h=24,
                      note=('Note', '[Non-GAAP measures are reconciled in the appendix. '
                                    'Δ is the change against the prior quarter.]'))
    assert end < 440, end
    return end


def main():
    d = Deck(DECK_NAME)
    page_summary(d)
    end = page_table(d)
    d.save(OUT)
    print(OUT, 'table end y =', end)


if __name__ == '__main__':
    main()
