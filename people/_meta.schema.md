# Meta schema (people)

Each `people/<slug>/` folder may include `meta.yml` to improve indexing.

```yaml
category: business | politics | strategy | philosophy | science | computing | economics | art

# optional
tags:
  - assistant   # sidekicks, chiefs of staff, right-hand operators
  - builder
  - thinker

aliases_by_lang:
  ja:
    - 日本語の一般的な名前
  zh:
    - 中文常用名
  ko:
    - 한국어 일반 표기
```

- `category` is used to group entries in the auto-generated README index.
- `tags` are used for additional curated sections (e.g., Assistants / Sidekicks).
- If `category` is missing, the index will put the entry under `Uncategorized`.
