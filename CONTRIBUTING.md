# Contributing

PR歓迎。人物追加も修正もOK。

## Quickstart: add a new profile

### Real people

1. Create a folder: `people/<slug>/`
2. Add 3 files:
   - `IDENTITY.md`
   - `SOUL.md`
   - `sources.md`
3. Open a PR.

### Fictional characters

We accept fiction under `fiction/`.

- Public domain: `fiction/public-domain/<slug>/`
- Modern works (inspired-by): `fiction/inspired/<slug>/`

See: `fiction/_guide.md`

## Slug rules

- lowercase + kebab-case: `steve-jobs`, `oda-nobunaga`
- prefer romanization for Japanese names.

## Quality bar

### Required
- `sources.md` is **required**.
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

- [ ] Has `sources.md`
- [ ] No personal attacks / speculation presented as fact
- [ ] SOUL is usable as agent configuration
