# Meta schema (fiction)

Each `fiction/**/<slug>/` folder may include `meta.yml` to improve indexing.

```yaml
# required
category: public-domain | inspired
work: "Title / Universe / Author"  # short human-readable reference

# optional
genre: mystery | horror | scifi | fantasy | drama | comedy | other
tags:
  - assistant

aliases_by_lang:
  ja:
    - 日本語の一般的な名前
  zh:
    - 中文常用名
  ko:
    - 한국어 일반 표기
```

- `category` and `genre` are used to group entries in the auto-generated README index.
- `tags` are used for additional curated sections (e.g., Assistants / Sidekicks).
- `work` is shown as a short note (avoid long quotes).
