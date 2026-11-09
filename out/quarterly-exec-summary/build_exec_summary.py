"""Build the Newmont quarterly financials executive summary template (2 content pages)."""
import os
import sys

sys.path.insert(0, '/Users/bpatel/dev/newmont-skill/scripts')
from newmont_kit import Deck, NAVY, SKY, MUTED, RULE_GREY, PP_ALIGN  # noqa: E402

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(OUT_DIR, 'newmont-quarterly-executive-summary.pptx')
DECK_NAME = 'Newmont – Q[X] 20XX Financial Results'

KPIS = (('GOLD PRODUCTION', '[0,000 koz]'),
        ('ALL-IN SUSTAINING COST', '[$0,000/oz]'),
        ('ADJUSTED EBITDA', '[$0.0B]'),
        ('FREE CASH FLOW', '[$0.0B]'))
DRIVERS = (('Production:', '[One sentence on volumes and the sites that moved them.]'),
           ('Costs:', '[One sentence on AISC and the main cost drivers.]'),
           ('Cash and balance sheet:', '[One sentence on free cash flow, net debt and shareholder returns.]'))
HEADER = ('Metric', 'Q[X] 20XX', 'Q[X−1] 20XX')
KEY_FIGURES = (('Revenue', '[$0.0B]', '[$0.0B]'),
               ('Adjusted net income per share', '[$0.00]', '[$0.00]'),
               ('Capital expenditure', '[$0.0B]', '[$0.0B]'),
               ('Net debt', '[$0.0B]', '[$0.0B]'),
               ('Dividend per share', '[$0.00]', '[$0.00]'))


def eyebrow(d, s, x, glyph_top, label, w=400):
    d.text(s, x, glyph_top, w, [label], 10.5, SKY, bold=True, em=0.015, caps=True)


def kpi_row(d, s):
    w, gap, y0, y1 = 214, 12, 100, 192
    for i, (label, value) in enumerate(KPIS):
        x = 36 + i * (w + gap)
        d.rect(s, x, y0, w, y1 - y0, SKY, alpha=0.10)
        eyebrow(d, s, x + 12, 112, label, w=w - 24)
        d.text(s, x + 12, 128, w - 24, [value], 24, NAVY, bold=True, em=-0.039)
        d.text(s, x + 12, 160, w - 24, ['[+0.0%] vs Q[X−1]', '[+0.0%] vs Q[X] prior year'],
               10, NAVY, em=0.009, pitch=11.8, h=26)


def drivers(d, s):
    eyebrow(d, s, 36, 216, 'WHAT DROVE THE QUARTER')
    paras, opts = [], []
    for k, (head, body) in enumerate(DRIVERS):
        paras += [[(head, True, False)], [(body, False, False)]]
        opts += [{'space_before': 12 if k else 0}, {}]
    d.text(s, 36, 239.5, 420, paras, 12, NAVY, em=0.008, pitch=18, h=155, opts=opts)


def key_figures(d, s):
    eyebrow(d, s, 487.5, 216, 'KEY FIGURES')
    cols, x0, x1, y, hgt = (487.5, 687.5, 807.5), 487.5, 928, 236, 21.6
    edges = cols + (x1,)
    for r, cells in enumerate((HEADER,) + KEY_FIGURES):
        bold = r == 0
        for i, c in enumerate(cells):
            w = edges[i + 1] - cols[i] - 11
            d.text(s, cols[i] + 7, y + 6, w, [c], 12, NAVY, bold=bold, em=0.004, pitch=14.3, h=16,
                   align=PP_ALIGN.RIGHT if i else None)
        y += hgt
        d.line(s, x0, y, x1, y, *((NAVY, 1.5) if bold else (RULE_GREY, 0.75)))


def outlook_and_note(d, s):
    d.line(s, 36, 392, 928, 392, NAVY, 0.5)
    eyebrow(d, s, 36, 404, 'OUTLOOK')
    d.text(s, 36, 421, 892, ['[One or two sentences on full-year guidance and the decisions the '
                             'executive team is asked to take.]'], 12, NAVY, em=0.008, pitch=18, h=20)
    d.text(s, 35.8, 448.7, 300, ['Note'], 10, MUTED, bold=True)
    d.text(s, 35.8, 460.8, 660, ['[Adjusted EBITDA, free cash flow and AISC are non-GAAP measures; '
                                 'see the reconciliation in the appendix.]'],
           10, MUTED, em=0.013, pitch=12, h=40)


def page_summary(d):
    s = d.blank('[Headline, e.g. Record free cash flow on higher gold prices]')
    eyebrow(d, s, 36, 83, 'EXECUTIVE SUMMARY | Q[X] 20XX')
    kpi_row(d, s)
    drivers(d, s)
    key_figures(d, s)
    outlook_and_note(d, s)


def page_table(d):
    d.table(title='[How the quarter compared with the prior quarter and guidance]',
            subtitle='Q[X] 20XX results against the prior quarter',
            header=HEADER,
            rows=[('Attributable gold production', '[0,000 koz]', '[0,000 koz]'),
                  ('Revenue', '[$0.0B]', '[$0.0B]'),
                  ('Adjusted net income', '[$0.0B]', '[$0.0B]'),
                  ('Adjusted EBITDA', '[$0.0B]', '[$0.0B]'),
                  ('Free cash flow', '[$0.0B]', '[$0.0B]'),
                  ('All-in sustaining cost', '[$0,000/oz]', '[$0,000/oz]'),
                  ('Net debt', '[$0.0B]', '[$0.0B]')],
            footnote=('Note', '[Non-GAAP measures are reconciled in the appendix.]'))


def main():
    d = Deck(DECK_NAME)
    page_summary(d)
    page_table(d)
    d.save(OUT)
    print(OUT)


if __name__ == '__main__':
    main()
