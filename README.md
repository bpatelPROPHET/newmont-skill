# newmont-skill

`newmont-brand` is a Claude skill that applies Newmont's visual identity to decks, documents and web pages, with the brand values hard-coded and a tested python-pptx kit.

## Layout

- `SKILL.md` – the skill: intake gate, page-type rules, brand system, kit usage, checker and reply format.
- `scripts/newmont_kit.py` – python-pptx kit, one method per page type, placeholders built in.
- `scripts/check_deck.py`, `scripts/inspect_pptx.py` – brand checker run on every deck before delivery.
- `evals/` – nine repeatability test cases in the `claude plugin eval` layout, plus `RESULTS-2026-11-05.md`.
- `TEST-PLAN.md` – how the skill was tested for repeatability and why.
- `docs/` – evaluation report (HTML and PDF).
- `out/` – sample outputs (quarterly executive summary template, original and v2).

## Using the skill

Copy or symlink this folder into `~/.claude/skills/newmont-brand/`. Requires `python-pptx`; LibreOffice for rendering previews; Open Sans installed as static TTFs for faithful previews.

## Running the evals

From this folder, with Claude Code installed:

```bash
claude plugin eval . --allow-tools Write,Edit,Bash --scaffold
```

The full workspace pattern (three runs per prompt, programmatic plus LLM grading, benchmark aggregation) is described in `TEST-PLAN.md` and `docs/evaluation-report.pdf`.
