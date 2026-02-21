# Greats Soul Archive

A community repository of **OpenClaw-style `IDENTITY.md` and `SOUL.md`** profiles for historical greats, philosophers, scientists, and high-impact builders.

## Why this exists

We want a world where you can *pick a mind* and have a real conversation:

- Talk to **Plato** about justice.
- Ask **Feynman** to explain something until it’s actually clear.
- Stress-test a product idea with **Jobs**-level taste.

Not as fan fiction — but as *usable agent configurations*.

This repo is the missing layer between biography and behavior: a compact, practical description of how a person thinks, decides, speaks, and fails.

## Principles

- **Separate sources (facts) from interpretation (agent persona).**
  - `sources.md` = references + confidence notes
  - `SOUL.md` / `IDENTITY.md` = an operational persona (how to act), grounded in sources
- Prefer clarity over cleverness.
- Make uncertainty explicit.
- Be especially conservative for living people.

## Repo structure

```
people/<slug>/
  IDENTITY.md   # short nameplate
  SOUL.md       # operating principles & style
  sources.md    # references (books, interviews, primary sources)

fiction/
  public-domain/<slug>/
  inspired/<slug>/
```

See: `fiction/_guide.md`

## Use cases

- Build a bot where users can choose a profile and **chat with their favorite philosopher**.
- Use `SOUL.md` as a “thinking style adapter” for writing, decision memos, or reviews.
- Teach: show how different mental models respond to the same prompt.

## Index

<!-- INDEX:START -->

### People

- [Alan Turing](people/alan-turing/)
- [Albert Einstein](people/albert-einstein/)
- [Aristotle](people/aristotle/)
- [Charles Darwin](people/charles-darwin/)
- [Claude Shannon](people/claude-shannon/)
- [Confucius](people/confucius/)
- [David Hume](people/david-hume/)
- [Elon Musk](people/elon-musk/)
- [Friedrich Nietzsche](people/friedrich-nietzsche/)
- [Galileo Galilei](people/galileo-galilei/)
- [Hannah Arendt](people/hannah-arendt/)
- [Immanuel Kant](people/immanuel-kant/)
- [Isaac Newton](people/isaac-newton/)
- [James Clerk Maxwell](people/james-clerk-maxwell/)
- [John Stuart Mill](people/john-stuart-mill/)
- [Ludwig Wittgenstein](people/ludwig-wittgenstein/)
- [Marie Curie](people/marie-curie/)
- [Masayoshi Son](people/masayoshi-son/)
- [Michael Faraday](people/michael-faraday/)
- [Oda Nobunaga](people/oda-nobunaga/)
- [Plato](people/plato/)
- [René Descartes](people/rene-descartes/)
- [Richard Feynman](people/richard-feynman/)
- [Steve Jobs](people/steve-jobs/)

### Fiction

- Public domain: `fiction/public-domain/` (no profiles yet)
- Inspired-by (modern works): `fiction/inspired/` (no profiles yet)
<!-- INDEX:END -->

## Contributing

PRs welcome — add a new person in ~10 minutes:

1. Create: `people/<slug>/`
2. Add: `IDENTITY.md`, `SOUL.md`, `sources.md` (**required**)
3. Open a PR

See: `CONTRIBUTING.md`

## Translations

- English: `README.md`
- Japanese: `README_ja.md`

(Additional languages welcome: `README_<lang>.md`)

## Notes / Disclaimer

- This is not academic history; it’s an **agent-design artifact**.
- Avoid defamation/harassment.
- If uncertain, mark uncertainty and/or add it to `sources.md`.

## License

CC0 1.0
