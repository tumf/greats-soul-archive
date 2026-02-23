# Contributing

PR歓迎。人物追加も修正もOK。

## Quickstart: add a new profile

### Real people

1. Create a folder: `people/<slug>/`
2. Add 3 files:
   - `IDENTITY.md`
   - `SOUL.md`
3. Open a PR.

### Fictional characters

We accept fiction under `fiction/`.

- Public domain: `fiction/public-domain/<slug>/`
- Modern works (inspired-by): `fiction/inspired/<slug>/`

See: `fiction/_guide.md`

## Optional: install the contributor skill

If you want a faster workflow, install the helper skill:

- Skill repo: https://github.com/tumf/skills
- Skill name: `greats-soul-archive-contributor`

Install:

```bash
npx skills add tumf/skills
```

Then use the scaffold script from the installed skill to generate a new profile folder.

## Keeping the index up to date

The README index is generated.

- Run: `python3 scripts/build_index.py`
- Don’t edit the index section by hand.

## Slug rules

- lowercase + kebab-case: `steve-jobs`, `oda-nobunaga`
- prefer romanization for Japanese names.

## Quality bar

### Required
- No defamation / hate / harassment.
- Separate **sources (facts)** from **SOUL/IDENTITY (interpretation for agents)**.

### Sources guidelines
- Prefer primary sources (speeches, letters, interviews, filings) when possible.
- If you cite books, include title + author + (optional) edition/year.
- If a claim is uncertain, mark it as such.

## Style

- Keep `IDENTITY.md` short.
- `SOUL.md` should be actionable (operating principles, communication style, failure modes).

## Review checklist

- [ ] No personal attacks / speculation presented as fact
- [ ] SOUL is usable as agent configuration
