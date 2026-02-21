# Meta schema (fiction)

Each `fiction/**/<slug>/` folder may include `meta.yml` to improve indexing.

```yaml
# required
category: public-domain | inspired
work: "Title / Universe / Author"  # short human-readable reference

# optional
genre: mystery | horror | scifi | fantasy | drama | comedy | other
aliases:
  - alternative display name
```

- `category` and `genre` are used to group entries in the auto-generated README index.
- `work` is shown as a short note (avoid long quotes).
