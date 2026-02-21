# Greats Soul Archive

歴史上の偉人・哲学者・科学者・偉大なビルダーたちを題材に、**OpenClaw風の `IDENTITY.md` / `SOUL.md`** を集めるコミュニティリポジトリ。

## これを作りたい理由

「好きな人物の“頭”を選んで会話できる世界」を作りたい。

- **プラトン**に正義を問い、
- **ファインマン**に“わかるまで”説明させ、
- **Jobs**の審美眼でプロダクト案を殴ってもらう。

これはファンフィクではなく、**使えるエージェント設定**としての人格モデル。

伝記（エピソードの集合）と、行動（会話でどう振る舞うか）の間にある「圧縮された思考様式」を、再利用できる形に落とす。

## 原則

- **史実の出典（facts）と、解釈/キャラ付け（agent persona）を分離**する
  - `sources.md` = 根拠リンク + 確度メモ
  - `SOUL.md` / `IDENTITY.md` = 出典に基づく“運用可能な人格”（どう考え、どう決め、どう話すか）
- うまいこと言うより、わかること。
- 不確実性は不確実と書く。
- 生存人物は特に保守的に。

## 構成

```
people/<slug>/
  IDENTITY.md   # エージェントの名札（短い）
  SOUL.md       # 行動規範・口調・価値観（長い）
  sources.md    # 根拠（伝記/インタビュー/書籍/一次情報など）

fiction/
  public-domain/<slug>/
  inspired/<slug>/
```

詳細: `fiction/_guide.md`

## 使い道

- ユーザーが人物を選んで、**好きな哲学者と話せるボット**を作る
- `SOUL.md` を“思考スタイル変換アダプタ”として、文章・意思決定・レビューに使う
- 教育用途：同じ問いに対して、異なるメンタルモデルがどう返すかを比較する

## インデックス

### ビルダー / ビジネス

- [Steve Jobs](people/steve-jobs/)
- [Elon Musk](people/elon-musk/)
- [Masayoshi Son](people/masayoshi-son/)
- [Oda Nobunaga](people/oda-nobunaga/)

### 哲学

- [Aristotle](people/aristotle/)
- [Plato](people/plato/)
- [Confucius](people/confucius/)
- [René Descartes](people/rene-descartes/)
- [David Hume](people/david-hume/)
- [Immanuel Kant](people/immanuel-kant/)
- [Friedrich Nietzsche](people/friedrich-nietzsche/)
- [John Stuart Mill](people/john-stuart-mill/)
- [Hannah Arendt](people/hannah-arendt/)
- [Ludwig Wittgenstein](people/ludwig-wittgenstein/)

### 科学 / 計算機

- [Isaac Newton](people/isaac-newton/)
- [Charles Darwin](people/charles-darwin/)
- [Marie Curie](people/marie-curie/)
- [Albert Einstein](people/albert-einstein/)
- [Richard Feynman](people/richard-feynman/)
- [Galileo Galilei](people/galileo-galilei/)
- [Michael Faraday](people/michael-faraday/)
- [James Clerk Maxwell](people/james-clerk-maxwell/)
- [Alan Turing](people/alan-turing/)
- [Claude Shannon](people/claude-shannon/)

### 架空人物

- Public domain: `fiction/public-domain/`
- Inspired-by（現行作品）: `fiction/inspired/`

## コントリビュート

PR歓迎。人物追加は最短10分：

1. `people/<slug>/` を作る
2. `IDENTITY.md` / `SOUL.md` / `sources.md`（必須）を追加
3. PRを出す

詳細: `CONTRIBUTING.md`

## README 翻訳

- 英語: `README.md`
- 日本語: `README_ja.md`

（他言語も歓迎: `README_<lang>.md`）

## 注意

- これは歴史研究ではなく、**エージェント設計用の成果物**。
- 誹謗・断定・ハラスメントはNG。
- 不確かな点は不確かと明記し、必要に応じて `sources.md` に根拠を足す。

## License

CC0 1.0
