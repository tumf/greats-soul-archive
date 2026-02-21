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
```

## Use cases

- Build a bot where users can choose a profile and **chat with their favorite philosopher**.
- Use `SOUL.md` as a “thinking style adapter” for writing, decision memos, or reviews.
- Teach: show how different mental models respond to the same prompt.

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
