---
name: newmont-brand
description: Newmont's visual identity, hard-coded and ready to apply. Use it whenever you create or restyle anything for Newmont or Newmont Corporation (slide decks and PowerPoint files, documents, reports, one-pagers, web pages, HTML artifacts, social or print graphics, charts, email headers) or when someone asks for content "in the Newmont style/brand/template", "on-brand for Newmont", or to fix a Newmont deck that looks off. Covers exact colours, Open Sans type scale with letter-spacing and line pitch, page geometry in points, the nine page types, logo (inline SVG and native PowerPoint shapes), photography and text-on-image rules, components, voice, and a tested python-pptx kit. Use it even if the request only mentions Newmont in passing. It starts with a short intake (content, format, photos, deck name and date) before anything is built, so nothing is assumed.
---

# Newmont brand

Everything here was measured from Newmont's "Visual Identity Refresh" deck (14 pages, 16:9) and then proven by rebuilding eight of its pages from these values alone and comparing them with the originals block by block: positions within 2 pt, the same fonts, sizes and colours, and the same line breaks for over 90% of text blocks. Use the numbers as given. Where something was not in the source deck (charts, icons, illustration), it is marked **suggested**.

Units: points (pt). The slide is 960 × 540 pt (13.333 × 7.5 in). 1 in = 72 pt; for screens 1 pt = 1.333 px, so the slide is 1280 × 720 px.

## How to use this skill

1. **Get the inputs.** Read "Before you build" and compare it with the request. If a must-have is missing, ask for it in one message and build nothing until it arrives. If the request already gives everything, do not ask anything.
2. **Map the content to page types** with the table in "Choosing page types", and write the page list down before coding.
3. **Run the setup check**, then build: PowerPoint with `scripts/newmont_kit.py` (never retype it); other formats as in "Other formats".
4. **Check and look.** Run `scripts/check_deck.py` on every deck, render it, and open the pages. Fix every FAIL.
5. **Deliver** with the reply format at the end: pages built, assumptions and placeholders, what was checked, any departure from the system.

If the person asks for something that breaks a rule (a new colour, a different font), do it, and say in one line that it departs from the Newmont system.

## Before you build: the inputs this skill cannot supply

The system below is measured to the point, so it reproduces whatever it is given, including guesses. Most bad Newmont outputs are not styling mistakes; they are correct styling applied to assumed content, invented figures, a made-up deck name on every footer, or stand-in photos. Your first job is to notice what you do not know and ask for it once, before writing any code.

**Must have.** If the request does not give these, stop and ask; do not build around them.

| Input | Why it blocks | If the person cannot supply it |
|---|---|---|
| **The content**: the actual points, figures, data, or a source document | A Newmont deliverable is read as fact. Never invent statistics, results, names or dates for it. | Offer to build the structure with bracketed placeholders like `[TRIFR 0.0]` and list every placeholder in the reply. |
| **The format** | "Deck" means PowerPoint; "intranet page" or "web" means HTML; "one-pager", "document" or "something for the board" could be any of them, and each is built differently. | Default to PowerPoint for anything called a deck or slides; otherwise ask. |
| **Photos**, when the pages need them (cover, closing, photo backdrop) | The kit crops real photo files into fixed boxes. Stock, generated or tinted images break the imagery rule and look wrong on sight. | Offer three options: send photos; build with sky-tile placeholders marked REPLACE where the photos go; or use dark-ground pages that need none. Never fetch or generate images. |
| **Deck name and date** (decks only) | The deck name is printed on every footer and the date on the cover. An invented one is wrong on every page. | Propose one from the subject ("Newmont – Q3 2026 Safety Performance", the current month) and say it is a proposal. |

**Decide and state.** Do not ask about these; use the default and name it at the top of your reply so it can be changed in one line.

- Length: what the content needs, one idea per page. Say the page count.
- Spelling: match the person's own writing; otherwise US.
- Audience and purpose: infer from the request ("exec team" means a short deck with a statement page and decisions; "intranet" means a plain, friendly page).
- File name: from the subject, lowercase with hyphens.
- Footer name of a web page or document: "Newmont – " plus the subject taken from the title ("Newmont – Tailings Management Update"). Say which you used.
- Callout style on the web: the sky 10% panel. Use the bordered box only when the panel would sit on another tint.
- Everything the skill already decides: colours, fonts, geometry, logo placement, footer text. Asking about these wastes the person's time.

**How to ask.** One message, numbered, normally four to six questions and never more than eight. Order them by how much they change the result (content first). End each with the default you will use if they say "just go", so a one-word answer is enough. Do not ask about anything the request already states. A complete brief gets zero questions: build at once. If the person says "just make it" or you are told to proceed with defaults, build with placeholders and open your reply with the list of assumptions. In an unattended run where no one can answer, write the questions down and stop rather than guess.

Example. Request: "put together a newmont deck on our Q3 safety performance for the exec team". Ask:
1. The Q3 figures (TRIFR, lost-time injuries, fatalities, high-potential incidents, with Q2 or the target for comparison), or the report they are in. Nothing is built without them.
2. The two or three messages the executives should leave with, and any decision you need from them.
3. Two approved photos, one of people and one wide site view. Default: marked placeholders.
4. Deck name and cover date. Default: "Newmont – Q3 2026 Safety Performance", November 2026.
5. Roughly how many slides. Default: 8 to 10.

Spelling, file name and audience are not asked: they are decided and stated in the reply. Request with the deck name, date, photos and every page's text given: no questions. Build it.

## Quick rules

- Font: **Open Sans** only, in Regular, Bold and Italic. Never Montserrat, Arial or system defaults for text.
- Colours: navy `#0C2B82`, deep navy `#071434`, sky `#12A6E6`, gold `#FCAF17`, white. Sky and gold are accents; gold is tiny.
- Light pages: white ground, navy text, sky for eyebrows, subheads and page numbers. Dark pages: deep navy ground, white text, sky eyebrows.
- Slide titles: 24 pt Bold, sentence case, a full-sentence statement, 1–2 lines, letter-spacing −0.039 em, top-left at 36 pt.
- Logo symbol top-right on every content page; sky logo tile on cover, section divider and closing.
- Footer on every page except cover and closing: deck name left, NEWMONT CORPORATION right, page number in sky.
- Flat design: no gradients, drop shadows, rounded corners, outlines or photo filters.
- Photography: real Newmont sites and people; never stock-looking, never tinted. White text on a photo only over a dark, calm area; otherwise use the white 70% panel.

## Colour

| Token | Hex | Use | Share of a typical deck |
|---|---|---|---|
| navy | `#0C2B82` | text on light grounds, section-divider ground, chevrons, table and column rules, logo N on light | ~7% |
| deep navy | `#071434` | ground for cover, closing and statement pages | ~20% |
| sky | `#12A6E6` | eyebrows, column subheads, numbered headings, page numbers, logo tile, 10% panels | ~6%, plus ~10% as tint |
| gold | `#FCAF17` | logo triangle, cover date; nothing else at text size | <1% |
| white | `#FFFFFF` | light ground; text on dark | ~45% |
| sky block | `#00A9EC` | large sky panel on section dividers only | — |
| gold block | `#FFAB00` | gold square on section dividers only | — |
| arrow navy | `#061641` | 1 pt timeline arrows | — |
| panel edge | `#010310` | 1 pt border of white panels over photos | — |
| footer grey | `#A6A6A6` on light, `#BFBFBF` on dark | footer text | — |
| muted grey | `#7F7F7F` | footnotes and their labels | — |
| rule grey | `#BFBFBF` | 0.75 pt table row rules | — |
| table total | `#EDEDEE` | total-row fill | — |
| milestone band | `#CEEEFB` | timeline milestone row | — |
| gantt row / pause | `#F2F2F2` / `#DFDFDF` | timeline rows / holiday column | — |

Tints: the sky panel is `#12A6E6` at **10% opacity** (renders `#E9F6FC` on white); a de-emphasised or optional column uses 5% (`#F6FAFC`). Panels over photos are white at **70% opacity** with a 1 pt `#010310` border.

Contrast (WCAG): navy on white 12.5:1, white on deep navy 18.1:1, sky on deep navy 6.6:1, gold on deep navy 9.7:1, navy on the divider sky 4.7:1. Sky on white is only 2.8:1, so use sky on white only for bold text of 10.5 pt and up (eyebrows, subheads), never for body copy.

## Typography

Install Open Sans as **static** files, one per weight (Regular, Bold, Italic, Bold Italic; for example from the googlefonts/opensans repository, `fonts/ttf/`). A variable Open Sans file makes LibreOffice fake the bold, which looks heavier and wider.

Letter-spacing (tracking) is given in em of the font size: in PowerPoint `spc` = em × size × 100; in CSS `letter-spacing: <em>em`. All text in the source is set slightly loose (+0.009 em); keep it, because it decides where lines wrap. Line pitch is the distance from one line to the next in points (PowerPoint: line spacing "Exactly"; CSS: line-height).

| Role | Size | Weight | Colour | Tracking | Line pitch | Notes |
|---|---|---|---|---|---|---|
| Closing display | 54 | Regular | white | −0.017 em | — | "Thank you!" |
| Section title | 48 | Regular | navy | −0.009 em | — | on the sky block |
| Cover title | 36 | Bold first line ("Newmont"), Regular after | white | −0.024 em | 39.8 | each line ≤ ~22 characters, max 4 lines |
| Slide title | 24 | Bold | navy; white on dark/photo | −0.039 em | 29.4 | ≤ 2 lines (≈ 70 characters per line at full width) |
| Statement | 24 | Regular | white | +0.002 em | 29.3 | lead statement on dark or photo; 12 pt between paragraphs |
| Callout title | 18 | Bold | navy | +0.008 em | 21 | inside panels on photos, centred |
| Callout line / subtitle | 16 | Italic (panels) or Bold (page subtitle) | navy | +0.008 / +0.02 em | — | |
| Column subhead | 14.5 | Bold | sky | −0.013 em | 16.3 | 2 lines |
| Body large | 12 | Regular, bold lead-in line | white or navy | +0.008 em | 18 | statement-page columns, tables (pitch 14.3) |
| Eyebrow | 10.5 | Bold, ALL CAPS | sky | +0.015 em | — | e.g. PURPOSE |
| Body | 10 | Regular; bold lead-ins inline | navy | +0.009 em | 11.8 | stand-alone bold labels +0.022 em |
| Caption | 8 | Bold | navy | 0 | — | above images and charts |
| Footer left | 8.5 | Regular, ALL CAPS | footer grey | +0.086 em | — | NEWMONT – DECK NAME |
| Footer right | 8 | Regular, ALL CAPS | footer grey | +0.108 em | — | NEWMONT CORPORATION |
| Page number | 8 | Regular | sky | +0.009 em | — | right-aligned to x 925 |
| Cover date | 7 | Bold, ALL CAPS | gold | +0.199 em | — | |

Lists (10 pt body): round bullet "•", hanging indent 13.5 pt (15.4 pt in the right-hand column of phase panels), 3 pt between items, 9 pt after the opening paragraph of a column, 12.5 pt extra for a blank line.

## Page geometry and furniture

Positions below are the **top-left of the first glyph** in pt, which is what you see. PowerPoint text boxes start higher: with zero internal margins, box top = glyph top − 0.317 × size for single-spaced text, or glyph top − (pitch − 0.887 × size) when line spacing is "Exactly". The kit does this for you.

- Margins: left 36, right ~32 (content ends by x 928), title glyph top 38.9, footer glyph top 519.2.
- Logo symbol: x 886.5, y 36.7, 42.1 × 37.6 pt (navy N on light, white N on dark; triangle always gold).
- Logo tile: 105.6 pt sky square; symbol inside at (34.3, 34.3), scale 0.953. The tile is the layout module: cover, divider and closing blocks snap to its edges.
- Footer: left text x 36; right text x 756.2; page number right edge 925. Section dividers keep only the page number.
- Two columns: x 36 and 487.5 (statement pages) or 36 and 493.5 (phase panels).
- Three columns: x 36 / 372.6 / 653.5, text widths 240 / 255 / 250; 0.5 pt navy vertical rules at x 351 and 634 from y 143 to 464; subhead glyph top 143.9; body 187.8; content (images, charts) from about y 240.

## Page types

### Cover (and closing)
Deep navy ground. Logo tile at (0, 0). Photo of people at (105.6, 105.8) 353.3 × 248.4. Wide operations photo at (458.9, 353.7) 501.1 × 186.3, bleeding off the right and bottom edges. Title block glyph top (500.4, 107.1): "Newmont" in Bold, then 1–3 Regular lines, 36 pt white, pitch 39.8; write it as short lines, each fitting 428 pt (≈ 22 characters). Date at (500.4, 310.3), 7 pt Bold caps gold. No footer, no page number.
Closing: same frame and photos; "Thank you!" 54 pt Regular white at (500.7, 277.5).

### Section divider
Navy ground. Sky block `#00A9EC` at (276.5, 0) 683.5 × 322.9. Logo tile at (0, 216.5). Gold block `#FFAB00` at (105.6, 322.9) 170.9 × 148.5. Title 48 pt Regular navy at (304.9, 252.2), one line, ≤ ~20 characters. Page number only.

### Statement on dark
Deep navy ground, white logo, footer. Title (white; pale `#D9E8EC` appears once in the source, do not copy). Eyebrow at (36, 116). Statement 24 pt at (36, 139.5), max width 640, ≤ 2 lines. Two columns from glyph top 234 (eyebrow) and 257.5 (items), x 36 and 487.5, width 380: each item is a bold 12 pt lead-in line then a 12 pt body (pitch 18), 18 pt between items, 2–3 items per column, body ≤ 3 lines.

### Content, three columns
White ground, navy logo, footer, 2-line title. Three columns as in the grid above: sky subhead (≤ 2 lines), 10 pt navy body (≤ 4 lines), then evidence: screenshots with a 0.25 pt black hairline (they may overlap in a cascade), charts, or numbers. Navy 0.5 pt rules between columns.

### Photo backdrop with panels
Full-bleed photo whose top-left is dark and calm (sky or shadow). White logo, footer in light grey. Title white, max width 451 (2 lines). Statement 24 pt white at (36, 159.5), width 500, ≤ 6 lines, 12 pt between paragraphs. Two white 70% panels with 1 pt `#010310` border: (36.4, 379.1) and (492.4, 378.4), each 432 × 101.3. Inside, centred: label and heading 18 pt Bold navy (pitch 21, first glyph 23.2 below the panel top), then one 16 pt Italic line 66.2 below the panel top.

### Phase panels (process, plan, scope)
White ground, title (often "Step 1: … | Key Steps"). "Objective" bold label at (36, 83.6), one-sentence body at (36, 95.6), width 540. Duration labels 10 pt Bold navy at (36, 144.1) and (493.5, 144.1), each followed by a 1 pt `#061641` arrow at y 147.4 starting 57.3 pt after the label and ending at x 475.7 / 928.3. Sky 10% panel at (20, 161.5) 916.8 × 342.9. Inside: sky bold numbered headings ("1. …") at y 179.7, x 36 / 493.5; body lists from y 203.7, widths 410 / 420, ≤ ~24 lines. An optional third column uses the 5% tint with light text.

### Table (fees, results, comparisons)
Title, optional subtitle 16 pt Bold navy at (36, 61.6). Table x 36–900, columns at 36 / 307 / 602, cell text inset 7 pt left and 6 pt from the row top, 12 pt navy (pitch 14.3). Header row 21.6 pt, Bold, 1.5 pt navy rule below. Body rows 36 pt, 0.75 pt `#BFBFBF` rule below each. Total row 21.6 pt, Bold, fill `#EDEDEE`. 1 pt white vertical separators at the column edges (only visible on filled rows). A secondary table below starts with a 1.5 pt navy rule on top. Footnote: 10 pt Bold `#7F7F7F` label at (35.8, 448.7) and 10 pt `#7F7F7F` text 12.1 below, width 660, pitch 12.

### Timeline (Gantt)
Week header row (bold number, date below), a `#CEEEFB` milestone band with navy star markers and 8 pt bold labels, `#F2F2F2` phase rows with navy `#0C2B82` chevron bars carrying white 12 pt italic durations, a `#DFDFDF` pause column (holidays), and dashed navy vertical milestone lines with 8 pt bold labels at the bottom.

### Plain content page
Title, logo, footer, and a body built from the components below, aligned to x 36 and the column positions above.

## Choosing page types

Pick the page type from the shape of the content, not from taste, so the same brief always becomes the same deck. Write the page list (number, type, title) before coding and put it in your reply.

| The content is… | Page type | Limits |
|---|---|---|
| The opening | Cover | title in short lines of ≤ 22 characters, 2–4 lines; two photos or placeholders |
| A new chapter in a deck of 8+ pages | Section divider | one line, ≤ 20 characters; skip dividers in shorter decks |
| One claim and the two to six points behind it | Statement on dark | statement ≤ 2 lines; 2–3 items per column, body ≤ 3 lines each |
| One claim with nothing under it (a decision, a purpose line) | Statement on dark, columns left out | same statement limits; still a statement page, not a blank page |
| Four or more items that each have a bold lead-in and one sentence (workstreams, risks and mitigations, actions and owners, questions and answers) | Lead-in list (`lead_in_list`, suggested) | up to 4 items per column, 8 per page; a 9th item starts a second page; never a table, tables are for numbers |
| Exactly three parallel points, each with a short explanation and optional evidence | Content, three columns | subhead ≤ 2 lines; body ≤ 4 lines; evidence below y 240; four or more points are a lead-in list, not two three-column pages |
| A mood or priorities page with a photo | Photo backdrop with panels | needs a photo with a dark, calm top-left; two panels |
| A process, plan or scope with two phases | Phase panels | ≤ ~24 lines per column; third column optional |
| Numbers in rows (fees, results, comparisons) | Table | 3 columns, ≤ 7 body rows, optional total and footnote; not for sentences |
| A schedule | Timeline (Gantt) | weeks across the top |
| A quarter's or year's results for executives | Financial summary page (suggested) | KPI tile row, drivers on the left, guidance or a chart on the right, outlook strip; see "Financial results pages" |
| Several metrics across periods with variances | Financial comparison table (`fin_table`, suggested) | up to 5 columns, numbers right-aligned, grouped rows, ≤ 12 body rows; one table per page |
| The close | Closing | "Thank you!" with the same photos as the cover |
| Anything else (a list, a chart, one paragraph) | Plain content page | build the body with the primitives on the column grid |

Rules: one idea per page; when text you wrote exceeds a limit, shorten it or split the page, never shrink the type; every deck is cover, content pages, closing, with dividers only when it has chapters. A four-point list is two statement pages or a plain page, not a cramped three-column page.

When the brief gives content but no page titles, write each title as a one-sentence statement drawn only from that page's own content, and list the titles you wrote under the assumptions in your reply.

**Default outline when only a topic is given** ("a deck on our Q3 safety performance", with figures to come or placeholders agreed): 8 pages, always in this order, so two builds of the same request match. 1 cover; 2 statement on dark with the headline and what went well / what needs attention; 3 table of the headline figures against the prior period and target; 4 plain content page with the trend chart (or a sky-tint box marked "CHART: replace" when there is no data); 5 three columns for the themes or drivers; 6 phase panels for the plan; 7 statement on dark with the decisions requested; 8 closing. Drop a page only when the person says the deck must be shorter, and say which one you dropped.

When text the person gave you exceeds a limit, keep their words and keep the measured geometry: build the page as given, and in the reply name the line that needs shortening and by roughly how much. Do not widen boxes, move neighbouring elements or shrink type to make it fit. Three builds of the same brief should produce the same page; the person decides what to cut.

## Restyling an existing deck

When asked to fix a deck that looks off, rebuild it with the kit rather than patching fonts and colours in place: patched files keep theme fonts, style references and shadows that come back when the deck is opened elsewhere. Steps: read every slide's text first; map each slide to a page type with the table above (a title-and-bullets slide becomes a plain content page or a statement page, three boxes become three columns); ask only for the deck name and the cover date if they are not in the file, with a proposed default; build; run the checker; reply with a short list of what changed (fonts, colours, shapes, furniture, structure) and anything you could not carry over.

"Keep the content" means every sentence word for word, in its original order and on its original slide, titles, credits and footers included. Change case (Title Case to sentence case), size, position and colour; do not rewrite titles into statements, reorder a line, drop a credit line, merge or add pages (no closing page unless the original had one). If a title would be better as a statement, offer the rewrite in the reply as a separate list, and leave the deck as the person wrote it. Photos the original lacks get the marked sky placeholders from "Making a deck", not blank navy.

## Financial results pages (suggested)

The source deck has no financial pages, so these are derived from its components and marked suggested; keep them unless the person has a measured Newmont results template, in which case use that. Two pages cover most quarterly reporting, and they must not repeat each other's numbers.

- **Financial summary page**: title is the one sentence the executives should remember; eyebrow "EXECUTIVE SUMMARY | Q[X] 20XX"; a row of four KPI tiles (`kpi_tiles`: label, value, two comparison lines each, chosen from production, AISC, adjusted EBITDA, free cash flow, revenue, net debt); left column "WHAT DROVE THE QUARTER" with three lead-ins (production, costs, cash and balance sheet); right column "AGAINST FULL-YEAR GUIDANCE" as a compact three-column mini table or, when there is trend data, a chart; a 0.5 pt navy rule, then "OUTLOOK AND DECISIONS" in one or two lines; the non-GAAP footnote.
- **Financial comparison table**: title says what moved; subtitle names the periods; `fin_table` at y 100 (it sits under the subtitle) with the unit in the first header cell ("USD millions unless stated"), three period columns (this quarter, prior quarter, same quarter last year) then one Δ column that compares with the prior quarter, rows grouped under sky caps labels (OPERATING, FINANCIAL, BALANCE SHEET AND RETURNS), numbers right-aligned, 24 pt rows, 8 to 10 body rows, the non-GAAP footnote. Only the metrics that are not already tiles on the summary page need full detail here; tiles may reappear only as table rows with the extra periods.

On the summary page the drivers and outlook are body large (12 pt, pitch 18) and the footnote keeps its 10 pt role; if something does not fit, cut a row or a line, never the type size.

Rules for numbers: units in the header or the row label, never in every cell; negative values with a minus sign, not parentheses, unless the person's own tables use parentheses; percentages with one decimal; a Δ column states what it compares against in the footnote.

**Templates.** When the person asks for a template rather than a filled deck, build the page with bracketed placeholders that show the format ("[$0.0B]", "[+0.0%]", "[0,000 koz]"), put an "e.g." example only in the title placeholder, and say in the reply which metrics and rows are suggestions to swap. A template still gets the full checker and render pass.

## Imagery

- Subjects: real operations and people — workers in hi-vis yellow and navy PPE with white branded hard hats, collaborating; haul trucks; aerial views of pits, stockpiles and conveyors. Natural, often golden-hour light; warm ochre and red earth against the navy palette. Documentary, sharp, no filters, no duotone, no tint.
- Shape: rectangles with square corners, no borders or shadows (except the 0.25 pt hairline on evidence screenshots).
- Placement: photos snap to the tile grid on cover and closing and may bleed off the right and bottom edges; full-bleed photos back statement pages.
- Text on photos: white text only where the photo under the text is dark and calm (median luminance ≤ 0.30, little texture); in practice the top-left sky or shadow. Where the area is busy or mid-toned, put the text in a white 70% panel with navy text. Never over faces or the main subject. On covers, text sits on the flat navy, not on the photos.
- Choose photos for the job: people for the cover's first photo, a wide operations view for the second; for a photo backdrop, a picture with a dark upper-left third.

## Components

- Sky panel: `#12A6E6` at 10%, square corners, no border, about 20 pt from the page edges.
- Column rule: 0.5 pt navy vertical line.
- Duration arrow: 10 pt bold navy label, then a 1 pt `#061641` line with a small triangular arrowhead.
- Chevron bar: navy pentagon/chevron with a white 12 pt italic label.
- Milestone: navy star with an 8 pt bold navy label.
- Callout box on light: 1 pt navy border, 10 pt body with a bold lead-in.
- Evidence thumbnail: screenshot with a 0.25 pt black frame, cascaded with overlaps.
- Charts (**suggested**, none in the source): series in the order navy, sky, deep navy, grey `#A6A6A6`; gold only to highlight one value; no 3D, no shadows; 0.5 pt `#D9D9D9` gridlines or none; labels 8–10 pt navy Open Sans; titles as 8 pt Bold captions.
- Icons (**suggested**, none in the source): simple navy line icons, about 1.5 pt stroke, no fills, no containers.

## Voice

- Titles are full-sentence assertions in sentence case ("The current system is built on strong base assets, but…"). Process pages may use "Step 1: … | Key Steps".
- Body: a bold lead-in, then one or two plain sentences. Lists for scope and steps. Numbered section headings in sky ("1. Masterbrand Identity Development").
- Eyebrows in ALL CAPS sky ("PURPOSE", "WHY WE NEED THIS…").
- Tone: confident, pragmatic, plain-spoken. The source mixes UK and US spelling; pick one per document (match the person's own).

## Logo

Use the symbol as supplied; never redraw, recolour the triangle, stretch, add effects, or place it on a busy photo without a dark calm area. Clear space: at least the triangle's height on all sides. Minimum size about 24 pt wide.

On light grounds (navy N):

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.12 37.57"><path fill="#0C2B82" d="M28.47 0V21.17L14.3 0H4.06V27.22L13.09 14.17L29.29 37.54H37.51V0Z"/><path fill="#FCAF17" d="M0 37.56H26.2L13.09 18.63Z"/><path fill="#0C2B82" d="M38.64 35.79V36.05H39.13V37.56H39.44V36.05H39.95V35.79ZM41.73 35.79L41.16 37.14L40.62 35.79H40.21V37.56H40.48V36.18L41.01 37.47H41.28L41.81 36.18V37.56H42.12V35.79Z"/></svg>
```

On dark grounds (white N):

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.12 37.57"><path fill="#FFFFFF" d="M28.47 0V21.17L14.3 0H4.06V27.22L13.09 14.17L29.29 37.54H37.51V0Z"/><path fill="#FCAF17" d="M0 37.56H26.2L13.09 18.63Z"/><path fill="#FFFFFF" d="M38.64 35.79V36.05H39.13V37.56H39.44V36.05H39.95V35.79ZM41.73 35.79L41.16 37.14L40.62 35.79H40.21V37.56H40.48V36.18L41.01 37.47H41.28L41.81 36.18V37.56H42.12V35.79Z"/></svg>
```

Logo tile (cover, divider, closing):

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 105.6 105.6"><rect width="105.6" height="105.6" fill="#12A6E6"/><g transform="translate(34.32 34.32) scale(0.953)"><path fill="#FFFFFF" d="M28.47 0V21.17L14.3 0H4.06V27.22L13.09 14.17L29.29 37.54H37.51V0Z"/><path fill="#FCAF17" d="M0 37.56H26.2L13.09 18.63Z"/><path fill="#FFFFFF" d="M38.64 35.79V36.05H39.13V37.56H39.44V36.05H39.95V35.79ZM41.73 35.79L41.16 37.14L40.62 35.79H40.21V37.56H40.48V36.18L41.01 37.47H41.28L41.81 36.18V37.56H42.12V35.79Z"/></g></svg>
```

The cover also sets the wordmark "Newmont" in Open Sans Bold as the first title line. No separate wordmark artwork was in the source; do not invent one.

## Making a deck (PowerPoint)

**Setup check**, before writing code:

```bash
python3 -c "import pptx" 2>/dev/null || pip install python-pptx
fc-list 2>/dev/null | grep -qi "open sans" && echo "Open Sans installed" || echo "Open Sans NOT installed"
which soffice || ls /Applications/LibreOffice.app/Contents/MacOS/soffice
```

If Open Sans is not installed, still set the font to Open Sans in the file (PowerPoint uses it wherever it is installed) and tell the person that your rendered preview used a substitute, so line breaks may differ slightly. The static TTFs are in the googlefonts/opensans repository under `fonts/ttf/`; on macOS they go in `~/Library/Fonts`. Never switch to another font to make the preview look right. If LibreOffice is missing, say that the deck was checked but not rendered.

**The kit** is `scripts/newmont_kit.py` next to this file. Copy it beside your build script and import it; never retype or trim it, and do not change its numbers. It draws the logo as native vector shapes, places every element at the measured positions, applies letter-spacing and line pitch, crops photos to fill their boxes, and removes the drop shadows python-pptx would otherwise add. Positions it takes are glyph tops in points, as in the page-type tables; `box_top()` converts them to text-box tops.

| Method | Builds |
|---|---|
| `Deck(deck_name)` | the presentation; `deck_name` is the footer text |
| `cover(title_lines, date, photo_people, photo_wide)` | cover; `title_lines` are the Regular lines after the bold "Newmont" |
| `closing(photo_people, photo_wide, text='Thank you!')` | closing page |
| `divider(name)` | section divider |
| `statement(title, eyebrow, statement, left_label=None, left_items=None, right_label=None, right_items=None)` | statement on dark; items are `(bold lead-in, body)`; leave them out for a statement that stands alone |
| `three_columns(title, columns)` | three columns; `columns` is 3 × `(subhead, body)` |
| `photo_panels(title, paragraphs, panels, photo)` | photo backdrop; `panels` is 2 × `(label, heading, italic line)` |
| `phase_panels(title, objective, phases)` | phase panels; see the docstring for the `phases` dicts |
| `table(title, subtitle, header, rows, total=None, footnote=None)` | table page |
| `lead_in_list(title, items, labels=(None, None), dark=False, numbered=False)` | up to 8 `(lead-in, body)` items in two columns; suggested, not measured |
| `kpi_tiles(s, tiles, y=100)` | on a `blank()` page: 3–4 sky-tint tiles of `(label, value, [lines])`; suggested |
| `fin_table(s, header, groups, y=150.6, col_w=None, row_h=26, note=None)` | on a `blank()` page: N-column financial table with right-aligned numbers and grouped rows; suggested |
| `blank(title, dark=False)` | title, logo and footer only; add the body with `text`, `rect`, `line`, `picture`, `logo` |
| `save(path)` | writes the file and strips the style references that add shadows |

Photo placeholders: when the person has no photos yet, pass `None` as the photo path. `cover`, `closing` and `picture` then draw the sky box with a white "PHOTO: …, replace" label at the measured position; never leave the box empty, draw the cover by hand, or pull in an image from elsewhere.

Example:

```python
from newmont_kit import Deck
d = Deck('Newmont – Q3 2026 Operations Review')            # footer text
d.cover(['Q3 2026 Operations', 'Review'], 'October 2026', 'people.jpg', 'pit.jpg')
d.divider('Performance')
d.three_columns('Output held steady while safety improved at every site',
                [('Production held at plan', 'Tier 1 sites offset slower ramp-up.'),
                 ('Safety improved in all regions', 'Recordable injuries fell again.'),
                 ('Costs are trending down', 'AISC eased as projects completed.')])
d.photo_panels('Two priorities will shape the fourth quarter', ['We will keep production on plan.'],
               [('Priority 1:', 'Sustain production', 'Hold output within 2% of plan'),
                ('Priority 2:', 'Complete autonomy', 'Bring two sites to full operation')], 'conveyor.jpg')
d.closing('people.jpg', 'pit.jpg')
d.save('q3-review.pptx')
```

Content rules the kit cannot enforce: keep within the line limits given for each page type (shorten or split instead of shrinking type), write cover titles as short lines, and add content inside columns and panels with the primitives (`text`, `rect`, `line`, `picture`, `logo`) on the same x positions.

## Other formats

**Web pages and HTML artifacts.** Scale 1 pt = 1.333 px for slide-sized pages; for normal web pages keep the ratios and use the type scale below.

```css
:root{
  --nm-navy:#0C2B82; --nm-deep:#071434; --nm-sky:#12A6E6; --nm-gold:#FCAF17; --nm-white:#FFFFFF;
  --nm-panel:rgba(18,166,230,.10); --nm-panel-ghost:rgba(18,166,230,.05); --nm-photo-panel:rgba(255,255,255,.70);
  --nm-grey:#A6A6A6; --nm-muted:#7F7F7F; --nm-rule:#BFBFBF;
  --nm-font:"Open Sans", "Segoe UI", Arial, sans-serif;
}
body{font-family:var(--nm-font);color:var(--nm-navy);letter-spacing:.009em}
.nm-title{font-weight:700;font-size:32px;line-height:39.2px;letter-spacing:-.039em}      /* 24pt / 29.4pt */
.nm-statement{font-weight:400;font-size:32px;line-height:39px;letter-spacing:.002em}
.nm-subhead{font-weight:700;font-size:19.3px;line-height:21.7px;letter-spacing:-.013em;color:var(--nm-sky)}
.nm-eyebrow{font-weight:700;font-size:14px;letter-spacing:.015em;text-transform:uppercase;color:var(--nm-sky)}
.nm-body{font-size:13.3px;line-height:15.7px}
.nm-body-lg{font-size:16px;line-height:24px}
.nm-footer{font-size:11.3px;letter-spacing:.086em;text-transform:uppercase;color:var(--nm-grey)}
.nm-panel{background:var(--nm-panel);border-radius:0}
.nm-dark{background:var(--nm-deep);color:#fff}
```

Load Open Sans from Google Fonts (weights 400 and 700, italic 400). Page skeleton, top to bottom: a deep navy header band with the white logo symbol top-right, holding the eyebrow, the title and the lead statement; the body on white with the columns separated by 0.5 pt navy rules; callouts in the sky 10% panel; a footer line in grey caps with the document name left and NEWMONT CORPORATION right. Keep square corners, no shadows, the logo symbol top-right, and the dark/light page logic. Open the page in a browser (or render it) before delivering; a page that was never looked at usually has one overflow.

**Documents (Word, PDF, Docs).** Title 24 pt Bold navy (−0.039 em); H2 14.5 pt Bold sky; eyebrows 10.5 pt Bold caps sky; body 10–11 pt navy Open Sans at about 1.2 line spacing; tables as in the table page type; logo symbol top-right of the first page; footer in 8–8.5 pt caps grey. Use the sky 10% panel for call-outs.

**Other tools.** Apply the same colours, Open Sans with the tracking values above, square corners and the photo rules. Where a tool cannot set letter-spacing, accept default spacing rather than switching fonts.

## Checking before delivering

For a deck, run the checker and fix every FAIL before anything else:

```bash
python3 scripts/check_deck.py deck.pptx --deck-name "Newmont – Deck name" --content-slides 3,4,5 --no-furniture-slides 1,6
```

It checks that every run is Open Sans (an inherited theme font fails, because it renders as Calibri), that every colour is in the palette, that nothing has a shadow, gradient, style reference or rounded corner, that the content slides carry the logo, footer and page number and the cover and closing do not, and the slide size. Then render and look at every page:

```bash
soffice --headless --convert-to pdf --outdir out deck.pptx
```

Open the PDF (or convert pages to PNG with pymupdf) and check what the script cannot: no text overflows its region, titles are ≤ 2 lines, cover lines are short, white text on photos sits only on dark calm areas, and each page is next to one of the same type from the source if you have it.

For HTML and documents, check the same things by hand: only Open Sans and the palette, no rounded corners, shadows or gradients, the logo top-right, eyebrows in sky caps, titles as sentence-case statements, and the text verbatim from the brief.

**Reply format.** Open with the assumptions and placeholders, if any. Then the pages built (number, type, title), what was checked (checker run, rendered and looked at, or why not; whether Open Sans was installed for the preview), and any departure from the system in one line each. Do not describe the brand rules back to the person.

## Things in the source not to copy

Montserrat in one footer, a pale `#D9E8EC` title on one dark page, titles without negative tracking on two pages, and mixed UK/US spelling. These are inconsistencies in the source, not rules.
