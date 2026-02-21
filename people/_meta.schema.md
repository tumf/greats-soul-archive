# Meta schema (people)

Each `people/<slug>/` folder may include `meta.yml` to improve indexing.

```yaml
category: business | politics | strategy | philosophy | science | computing | economics | art
# optional
aliases:
  - alternative display name
```

- `category` is used to group entries in the auto-generated README index.
- If missing, the index will put the entry under `Uncategorized`.
