"""Newmont deck kit: python-pptx, all brand values hard-coded. Requires: pip install python-pptx
Positions below are the GLYPH TOPS measured in the source deck (pt); box_top() turns them into text-box tops."""
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn

NAVY, DEEP, SKY, GOLD, WHITE = '0C2B82', '071434', '12A6E6', 'FCAF17', 'FFFFFF'
SKY_BLOCK, GOLD_BLOCK, ARROW, PANEL_EDGE = '00A9EC', 'FFAB00', '061641', '010310'
GREY_L, GREY_D, MUTED, RULE_GREY, TOTAL_FILL = 'A6A6A6', 'BFBFBF', '7F7F7F', 'BFBFBF', 'EDEDEE'
FONT = 'Open Sans'
BASE_EM, LABEL_EM = 0.009, 0.022          # all text +0.009em; stand-alone bold labels (<=10.5pt) +0.022em
LOGO = {  # symbol, 42.12 x 37.57 pt at 100%; polygons in pt
    'n': [(28.47, 0), (28.47, 21.17), (14.3, 0), (4.06, 0), (4.06, 27.22), (13.09, 14.17), (29.29, 37.54), (37.51, 37.54), (37.51, 0)],
    'triangle': [(0, 37.56), (26.2, 37.56), (13.09, 18.63)],
    'tm_t': [(38.64, 35.79), (38.64, 36.05), (39.13, 36.05), (39.13, 37.56), (39.44, 37.56), (39.44, 36.05), (39.95, 36.05), (39.95, 35.79)],
    'tm_m': [(41.73, 35.79), (41.16, 37.14), (40.62, 35.79), (40.21, 35.79), (40.21, 37.56), (40.48, 37.56), (40.48, 36.18), (41.01, 37.47),
             (41.28, 37.47), (41.81, 36.18), (41.81, 37.56), (42.12, 37.56), (42.12, 35.79)]}

def box_top(glyph_top, size, pitch=None):
    """Text-box top (zero insets) that puts the first glyph top at glyph_top. Calibrated in LibreOffice;
    PowerPoint lands within about 1pt."""
    return glyph_top - ((pitch - 0.8873 * size) if pitch else 0.3167 * size)

class Deck:
    def __init__(self, deck_name='Newmont – Presentation'):
        self.p = Presentation(); self.p.slide_width, self.p.slide_height = Pt(960), Pt(540)
        self.deck_name = deck_name

    # ---------- primitives ----------
    def _slide(self, ground):
        s = self.p.slides.add_slide(self.p.slide_layouts[6])
        s.background.fill.solid(); s.background.fill.fore_color.rgb = RGBColor.from_string(ground); return s
    @property
    def n(self): return len(self.p.slides)
    def rect(self, s, x, y, w, h, fill, alpha=None, edge=None, edge_w=1):
        sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Pt(x), Pt(y), Pt(w), Pt(h))
        sh.fill.solid(); sh.fill.fore_color.rgb = RGBColor.from_string(fill)
        if alpha is not None:
            c = sh.fill._xPr.find(qn('a:solidFill'))[0]; c.append(c.makeelement(qn('a:alpha'), {'val': str(int(alpha * 100000))}))
        if edge: sh.line.color.rgb = RGBColor.from_string(edge); sh.line.width = Pt(edge_w)
        else: sh.line.fill.background()
        return sh
    def line(self, s, x0, y0, x1, y1, color, w, arrow=False, dash=False):
        ln = s.shapes.add_connector(1, Pt(x0), Pt(y0), Pt(x1), Pt(y1)); ln.line.color.rgb = RGBColor.from_string(color); ln.line.width = Pt(w)
        el = ln.line._get_or_add_ln()
        if dash: el.append(el.makeelement(qn('a:prstDash'), {'val': 'dash'}))
        if arrow: el.append(el.makeelement(qn('a:tailEnd'), {'type': 'triangle'}))
        return ln
    def text(self, s, x, glyph_top, w, paras, size, color, bold=False, italic=False, em=None, pitch=None,
             align=None, caps=False, h=None, opts=None, anchor_box_top=None):
        """paras: list of str or list of (text, bold, italic) runs; '\\v' = line break. One call per text flow."""
        top = anchor_box_top if anchor_box_top is not None else box_top(glyph_top, size, pitch)
        tb = s.shapes.add_textbox(Pt(x), Pt(top), Pt(w), Pt(h or size * 2)); tf = tb.text_frame
        tf.word_wrap = True; tf.auto_size = None; tf.vertical_anchor = MSO_ANCHOR.TOP
        for m in ('margin_left', 'margin_right', 'margin_top', 'margin_bottom'): setattr(tf, m, 0)
        for i, para in enumerate(paras):
            o = (opts or [{}] * len(paras))[i]
            pp = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            if align: pp.alignment = align
            if pitch: pp.line_spacing = Pt(pitch)
            if i and o.get('space_before'): pp.space_before = Pt(o['space_before'])
            if o.get('bullet'):
                ind = o.get('indent', 13.5); pPr = pp._p.get_or_add_pPr()
                pPr.set('marL', str(int(Pt(ind)))); pPr.set('indent', str(-int(Pt(ind))))
                pPr.append(pPr.makeelement(qn('a:buFont'), {'typeface': 'Arial'})); pPr.append(pPr.makeelement(qn('a:buChar'), {'char': '•'}))
            runs = [(para, bold, italic)] if isinstance(para, str) else para
            for t, b, it in runs:
                for j, part in enumerate(t.split('\v')):
                    if j: pp.add_line_break()
                    if not part: continue
                    r = pp.add_run(); r.text = part.upper() if caps else part; f = r.font
                    sz = o.get('size', size); f.name = FONT; f.size = Pt(sz); f.bold = b; f.italic = it
                    f.color.rgb = RGBColor.from_string(o.get('color', color))
                    e = em if em is not None else (LABEL_EM if b and len(runs) == 1 and sz <= 10.5 else BASE_EM)
                    r._r.get_or_add_rPr().set('spc', str(round(e * sz * 100)))
        return tb
    def logo(self, s, x, y, scale=1.0, mark=NAVY, tm=True):
        """Native vector symbol. Light grounds: mark=NAVY. Dark grounds/tiles: mark=WHITE. Triangle always gold."""
        for part, col in (('triangle', GOLD), ('n', mark)) + ((('tm_t', mark), ('tm_m', mark)) if tm else ()):
            pts = LOGO[part]; fb = s.shapes.build_freeform(Pt(x + pts[0][0] * scale), Pt(y + pts[0][1] * scale))
            fb.add_line_segments([(Pt(x + px * scale), Pt(y + py * scale)) for px, py in pts[1:]], close=True)
            sh = fb.convert_to_shape(); sh.fill.solid(); sh.fill.fore_color.rgb = RGBColor.from_string(col); sh.line.fill.background()
    def corner_logo(self, s, dark): self.logo(s, 886.5, 36.7, 1.0, WHITE if dark else NAVY)
    def tile(self, s, x, y):
        self.rect(s, x, y, 105.6, 105.6, SKY); self.logo(s, x + 34.32, y + 34.32, 0.953, WHITE)
    def footer(self, s, dark, number=True, full=True):
        g = GREY_D if dark else GREY_L
        if full:
            self.text(s, 36, 519.2, 400, [self.deck_name], 8.5, g, em=0.086, caps=True)
            self.text(s, 756.2, 519.4, 160, ['Newmont Corporation'], 8, g, em=0.108, caps=True)
        if number: self.text(s, 885, 519.4, 40, [str(self.n)], 8, SKY, align=PP_ALIGN.RIGHT)
    def title(self, s, txt, dark=False, width=840):
        self.text(s, 36, 38.9, width, [txt], 24, WHITE if dark else NAVY, bold=True, em=-0.039, pitch=29.4, h=70)
    def picture(self, s, path, x, y, w, h, label='PHOTO: replace'):
        """Place an image filling the box (centre crop), square corners, no effects.
        path=None (or a missing file) draws the marked sky placeholder instead, so decks without photos still build."""
        import os
        if not path or not os.path.exists(path):
            self.rect(s, x, y, w, h, SKY)
            self.text(s, x + 10, y + 10, w - 20, [label], 10, WHITE, bold=True)
            return None
        pic = s.shapes.add_picture(path, Pt(x), Pt(y), Pt(w), Pt(h)); iw, ih = pic.image.size
        ar_img, ar_box = iw / ih, w / h
        if ar_img > ar_box: c = (1 - ar_box / ar_img) / 2; pic.crop_left = pic.crop_right = c
        else: c = (1 - ar_img / ar_box) / 2; pic.crop_top = pic.crop_bottom = c
        return pic

    # ---------- archetypes ----------
    def cover(self, title_lines, date, photo_people, photo_wide, brand='Newmont'):
        s = self._slide(DEEP); self.tile(s, 0, 0)
        self.picture(s, photo_people, 105.6, 105.8, 353.3, 248.4, label='PHOTO: people, replace')
        self.picture(s, photo_wide, 458.9, 353.7, 501.1, 186.3, label='PHOTO: wide operations view, replace')
        self.text(s, 500.4, 107.1, 428, [[(brand, True, False)]] + list(title_lines), 36, WHITE, em=-0.024, pitch=39.8, h=200)
        self.text(s, 500.4, 310.3, 200, [date], 7, GOLD, bold=True, em=0.199, caps=True)
        return s
    def closing(self, photo_people, photo_wide, text='Thank you!'):
        s = self._slide(DEEP); self.tile(s, 0, 0)
        self.picture(s, photo_people, 105.6, 105.8, 353.3, 248.4, label='PHOTO: people, replace')
        self.picture(s, photo_wide, 458.9, 353.7, 501.1, 186.3, label='PHOTO: wide operations view, replace')
        self.text(s, 500.7, 277.5, 420, [text], 54, WHITE, em=-0.017, h=80)
        return s
    def divider(self, name):
        s = self._slide(NAVY)
        self.rect(s, 276.5, 0, 683.5, 322.9, SKY_BLOCK); self.rect(s, 105.6, 322.9, 170.9, 148.5, GOLD_BLOCK)
        self.tile(s, 0, 216.5)
        self.text(s, 304.9, 252.2, 620, [name], 48, NAVY, em=-0.009, h=70)
        self.footer(s, dark=True, full=False)
        return s
    def statement(self, title, eyebrow, statement, left_label=None, left_items=None, right_label=None, right_items=None):
        """left/right_items: [(bold lead-in, body sentence), ...]; 2-3 items per column.
        Leave the items out for a statement that stands alone (a decision, a purpose line)."""
        s = self._slide(DEEP); self.corner_logo(s, True); self.footer(s, True); self.title(s, title, dark=True)
        self.text(s, 36, 116, 400, [eyebrow], 10.5, SKY, bold=True, em=0.015, caps=True)
        self.text(s, 36, 139.5, 640, [statement], 24, WHITE, em=0.002, pitch=29.3, h=70)
        for x, lab, items in ((36, left_label, left_items), (487.5, right_label, right_items)):
            if not items: continue
            self.text(s, x, 234, 400, [lab], 10.5, SKY, bold=True, em=0.015, caps=True)
            paras, opts = [], []
            for k, (head, body) in enumerate(items):
                paras += [[(head, True, False)], [(body, False, False)]]; opts += [{'space_before': 18 if k else 0}, {}]
            self.text(s, x, 257.5, 380, paras, 12, WHITE, em=0.008, pitch=18, h=260, opts=opts)
        return s
    def three_columns(self, title, columns, divider_lines=True):
        """columns: 3 x (subhead, body). Content (images, charts) goes below y=240 inside each column."""
        s = self._slide(WHITE); self.corner_logo(s, False); self.footer(s, False); self.title(s, title)
        for (head, body), x, w in zip(columns, (36, 372.6, 653.5), (240, 255, 250)):
            self.text(s, x, 143.9, w, [head], 14.5, SKY, bold=True, em=-0.013, pitch=16.3, h=40)
            self.text(s, x, 187.8, w, [body], 10, NAVY, pitch=11.8, h=60)
        if divider_lines:
            for x in (351, 634): self.line(s, x, 143, x, 464, NAVY, 0.5)
        return s
    def photo_panels(self, title, paragraphs, panels, photo):
        """Full-bleed photo with a dark, calm top-left; panels: 2 x (label, heading, italic line)."""
        s = self._slide(DEEP); self.picture(s, photo, 0, 0, 960, 540)
        self.corner_logo(s, True); self.footer(s, True); self.title(s, title, dark=True, width=451)
        self.text(s, 36, 159.5, 500, paragraphs, 24, WHITE, em=0.002, pitch=29.3, h=200,
                  opts=[{}] + [{'space_before': 12}] * (len(paragraphs) - 1))
        for (lab, head, sub), (x, y) in zip(panels, ((36.4, 379.1), (492.4, 378.4))):
            self.rect(s, x, y, 432, 101.3, WHITE, alpha=0.70, edge=PANEL_EDGE)
            self.text(s, x, None, 432, [[(lab, True, False)], [(head, True, False)]], 18, NAVY, em=0.008, pitch=21,
                      align=PP_ALIGN.CENTER, anchor_box_top=y + 18.2, h=50)
            self.text(s, x, y + 23.2 + 43, 432, [sub], 16, NAVY, italic=True, em=0.008, align=PP_ALIGN.CENTER)
        return s
    def phase_panels(self, title, objective, phases):
        """phases: 2 x dict(duration='2.5 weeks', heading='1. ...', items=[('p'|'b'|'gap', text or runs)])."""
        s = self._slide(WHITE); self.corner_logo(s, False); self.footer(s, False); self.title(s, title)
        self.text(s, 36, 83.6, 300, ['Objective'], 10, NAVY, bold=True)
        self.text(s, 36, 95.6, 540, [objective], 10, NAVY, pitch=11.8, h=30)
        self.rect(s, 20, 161.5, 916.8, 342.9, SKY, alpha=0.10)
        for ph, x, end, w in zip(phases, (36, 493.5), (475.7, 928.3), (410, 420)):
            self.text(s, x, 144.1, 80, [ph['duration']], 10, NAVY, bold=True)
            self.line(s, x + 57.3, 147.4, end, 147.4, ARROW, 1, arrow=True)
            self.text(s, x, 179.7, 420, [ph['heading']], 10, SKY, bold=True)
            paras, opts, gap = [], [], False
            for kind, val in ph['items']:
                if kind == 'gap': gap = True; continue
                sp = 0 if not paras else (9 if len(paras) == 1 else 3) + (12.5 if gap else 0); gap = False
                paras.append([(val, False, False)] if isinstance(val, str) else val)
                opts.append({'space_before': sp, 'bullet': kind == 'b', 'indent': 13.5 if x == 36 else 15.4})
            self.text(s, x, 203.7, w, paras, 10, NAVY, pitch=11.8, h=290, opts=opts)
        return s
    def table(self, title, subtitle, header, rows, total=None, footnote=None):
        """header: 3 strings; rows: list of 3 cells (str or runs); total: 3 cells; footnote: (label, text)."""
        s = self._slide(WHITE); self.corner_logo(s, False); self.footer(s, False); self.title(s, title)
        if subtitle: self.text(s, 36, 61.6, 700, [subtitle], 16, NAVY, bold=True, em=0.02)
        cols, x0, x1, y = (36, 307, 602), 36, 900, 150.6
        def row(cells, hgt, bold, fill=None, rule=(RULE_GREY, 0.75)):
            nonlocal y
            if fill: self.rect(s, x0, y, x1 - x0, hgt, fill)
            for i, c in enumerate(cells):
                w = (cols + (x1,))[i + 1] - cols[i] - 11
                self.text(s, cols[i] + 7, y + 6, w, [c], 12, NAVY,
                          bold=bold, em=0.004, pitch=14.3, h=30)
            for cx in cols[1:]: self.line(s, cx, y, cx, y + hgt, WHITE, 1)
            y += hgt; self.line(s, x0, y, x1, y, *rule)
        row(header, 21.6, True, rule=(NAVY, 1.5))
        for r in rows: row(r, 36, False)
        if total: row(total, 21.6, True, fill=TOTAL_FILL)
        if footnote:
            self.text(s, 35.8, 448.7, 300, [footnote[0]], 10, MUTED, bold=True)
            self.text(s, 35.8, 460.8, 660, [footnote[1]], 10, MUTED, em=0.013, pitch=12, h=40)
        return s
    def kpi_tiles(self, s, tiles, y=100, h=92):
        """SUGGESTED (not measured from the source deck): a row of 3 or 4 KPI tiles across x 36-928, 12pt gaps.
        tiles: [(label, value, [line1, line2]), ...]; the lines list may be empty."""
        gap = 12; w = (892 - gap * (len(tiles) - 1)) / len(tiles)
        for i, (label, value, lines) in enumerate(tiles):
            x = 36 + i * (w + gap)
            self.rect(s, x, y, w, h, SKY, alpha=0.10)
            self.text(s, x + 12, y + 12, w - 24, [label], 10.5, SKY, bold=True, em=0.015, caps=True)
            self.text(s, x + 12, y + 28, w - 24, [value], 24, NAVY, bold=True, em=-0.039)
            if lines: self.text(s, x + 12, y + 60, w - 24, list(lines[:2]), 10, NAVY, pitch=11.8, h=26)
    def fin_table(self, s, header, groups, y=150.6, col_w=None, row_h=26, note=None):
        """SUGGESTED (not measured from the source deck): N-column financial table across x 36-928; first column
        left-aligned, the rest right-aligned. col_w: widths of columns 2..N (default 420pt split equally).
        groups: [(group_label or None, rows)], rows: lists of N str; a final row starting 'Total' is bold on
        TOTAL_FILL. note: (label, text) footnote. Returns the y where the table ends."""
        n = len(header); col_w = list(col_w) if col_w else [420 / (n - 1)] * (n - 1)
        x0, x1 = 36, 928; widths = [x1 - x0 - sum(col_w)] + col_w
        edges = [x0]
        for cw in widths: edges.append(edges[-1] + cw)
        last = groups[-1][1][-1] if groups and groups[-1][1] else None
        def row(cells, hgt, bold, fill=None, rule=(RULE_GREY, 0.75)):
            nonlocal y
            if fill: self.rect(s, x0, y, x1 - x0, hgt, fill)
            for i, c in enumerate(cells):
                self.text(s, edges[i] + 7, y + 6, widths[i] - 14, [c], 12, NAVY, bold=bold, em=0.004, pitch=14.3,
                          h=16, align=PP_ALIGN.RIGHT if i else None)
            y += hgt; self.line(s, x0, y, x1, y, *rule)
        row(header, 21.6, True, rule=(NAVY, 1.5))
        for label, rows in groups:
            if label is not None:
                self.text(s, x0 + 7, y + 6, widths[0] - 14, [label], 10.5, SKY, bold=True, em=0.015, caps=True)
                y += 20
            for r in rows:
                tot = r is last and str(r[0]).startswith('Total')
                row(r, row_h, tot, fill=TOTAL_FILL if tot else None)
        if note:
            self.text(s, 35.8, 448.7, 300, [note[0]], 10, MUTED, bold=True)
            self.text(s, 35.8, 460.8, 660, [note[1]], 10, MUTED, em=0.013, pitch=12, h=40)
        return y
    def lead_in_list(self, title, items, labels=(None, None), dark=False, numbered=False):
        """SUGGESTED (not in the source deck): a list of up to 8 items that each have a bold lead-in and one
        sentence (risks and mitigations, actions and owners, questions and answers). Two columns at the
        statement-page x positions, up to 4 items per column; more than 8 items means a second page.
        items: [(lead-in, body), ...]; labels: optional sky eyebrows over each column."""
        s = self.blank(title, dark); col = WHITE if dark else NAVY
        for k, (x, lab) in enumerate(((36, labels[0]), (487.5, labels[1]))):
            chunk = items[k * 4:(k + 1) * 4]
            if not chunk: continue
            if lab: self.text(s, x, 116, 400, [lab], 10.5, SKY, bold=True, em=0.015, caps=True)
            paras, opts = [], []
            for i, (head, body) in enumerate(chunk):
                n = k * 4 + i + 1
                paras += [[(('%d. ' % n if numbered else '') + head, True, False)], [(body, False, False)]]
                opts += [{'space_before': 18 if i else 0}, {}]
            self.text(s, x, 139.5, 420, paras, 12, col, em=0.008, pitch=18, h=330, opts=opts)
        return s
    def blank(self, title, dark=False):
        """Light or dark content page with title, logo and footer only; build the body with the primitives."""
        s = self._slide(DEEP if dark else WHITE); self.corner_logo(s, dark); self.footer(s, dark); self.title(s, title, dark)
        return s

    def save(self, path):
        for sl in self.p.slides:      # remove python-pptx theme style refs (they add drop shadows)
            for st in list(sl.shapes._spTree.iter(qn('p:style'))): st.getparent().remove(st)
        self.p.save(path)
