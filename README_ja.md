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

<!-- INDEX_JA:START -->

### People（実在）

- [Abraham Lincoln](people/abraham-lincoln/)
- [Ada Lovelace](people/ada-lovelace/)
- [Adam Smith](people/adam-smith/)
- [Alan Kay](people/alan-kay/)
- [Alan Turing](people/alan-turing/)
- [Albert Einstein](people/albert-einstein/)
- [Alexander the Great](people/alexander-the-great/)
- [Amos Tversky](people/amos-tversky/)
- [Andy Grove](people/andy-grove/)
- [Angela Merkel](people/angela-merkel/)
- [Aristotle](people/aristotle/)
- [Augustus](people/augustus/)
- [Barbara McClintock](people/barbara-mcclintock/)
- [Bill Gates](people/bill-gates/)
- [Bjarne Stroustrup](people/bjarne-stroustrup/)
- [Brendan Eich](people/brendan-eich/)
- [Carl Sagan](people/carl-sagan/)
- [Carl von Clausewitz](people/carl-von-clausewitz/)
- [Catherine the Great](people/catherine-the-great/)
- [Charles Darwin](people/charles-darwin/)
- [Charlie Munger](people/charlie-munger/)
- [Claude Shannon](people/claude-shannon/)
- [Confucius](people/confucius/)
- [Daniel Kahneman](people/daniel-kahneman/)
- [David Hume](people/david-hume/)
- [Dennis Ritchie](people/dennis-ritchie/)
- [Derek Parfit](people/derek-parfit/)
- [Donald Knuth](people/donald-knuth/)
- [Elinor Ostrom](people/elinor-ostrom/)
- [Elon Musk](people/elon-musk/)
- [Emmy Noether](people/emmy-noether/)
- [Epictetus](people/epictetus/)
- [Franklin D. Roosevelt](people/franklin-d-roosevelt/)
- [Friedrich Nietzsche](people/friedrich-nietzsche/)
- [Fyodor Dostoevsky](people/fyodor-dostoevsky/)
- [Galileo Galilei](people/galileo-galilei/)
- [Grace Hopper](people/grace-hopper/)
- [Guido van Rossum](people/guido-van-rossum/)
- [Hannah Arendt](people/hannah-arendt/)
- [Hannibal](people/hannibal/)
- [Haruki Murakami](people/haruki-murakami/)
- [Herbert A. Simon](people/herbert-a-simon/)
- [Howard Schultz](people/howard-schultz/)
- [Immanuel Kant](people/immanuel-kant/)
- [Indra Nooyi](people/indra-nooyi/)
- [Isaac Newton](people/isaac-newton/)
- [Jack Ma](people/jack-ma/)
- [Jack Welch](people/jack-welch/)
- [James Clerk Maxwell](people/james-clerk-maxwell/)
- [James Gosling](people/james-gosling/)
- [James Joyce](people/james-joyce/)
- [Jane Austen](people/jane-austen/)
- [Jeff Bezos](people/jeff-bezos/)
- [Jensen Huang](people/jensen-huang/)
- [John Carmack](people/john-carmack/)
- [John Maynard Keynes](people/john-maynard-keynes/)
- [John Rawls](people/john-rawls/)
- [John Stuart Mill](people/john-stuart-mill/)
- [John von Neumann](people/john-von-neumann/)
- [Julius Caesar](people/julius-caesar/)
- [Karl Popper](people/karl-popper/)
- [Ken Thompson](people/ken-thompson/)
- [Kierkegaard](people/kierkegaard/)
- [Lee Kuan Yew](people/lee-kuan-yew/)
- [Leo Tolstoy](people/leo-tolstoy/)
- [Leonardo da Vinci](people/leonardo-da-vinci/)
- [Linus Torvalds](people/linus-torvalds/)
- [Ludwig Wittgenstein](people/ludwig-wittgenstein/)
- [Mahatma Gandhi](people/mahatma-gandhi/)
- [Marc Andreessen](people/marc-andreessen/)
- [Marcus Aurelius](people/marcus-aurelius/)
- [Margaret Hamilton](people/margaret-hamilton/)
- [Margaret Thatcher](people/margaret-thatcher/)
- [Marie Curie](people/marie-curie/)
- [Mary Barra](people/mary-barra/)
- [Masayoshi Son](people/masayoshi-son/)
- [Max Planck](people/max-planck/)
- [Michael Faraday](people/michael-faraday/)
- [Michel Foucault](people/michel-foucault/)
- [Milton Friedman](people/milton-friedman/)
- [Miyamoto Musashi](people/miyamoto-musashi/)
- [Napoleon Bonaparte](people/napoleon-bonaparte/)
- [Nelson Mandela](people/nelson-mandela/)
- [Niels Bohr](people/niels-bohr/)
- [Nikola Tesla](people/nikola-tesla/)
- [Oda Nobunaga](people/oda-nobunaga/)
- [Oprah Winfrey](people/oprah-winfrey/)
- [Otto von Bismarck](people/otto-von-bismarck/)
- [Paul Graham](people/paul-graham/)
- [Peter Thiel](people/peter-thiel/)
- [Plato](people/plato/)
- [Pony Ma](people/pony-ma/)
- [Queen Elizabeth I](people/queen-elizabeth-i/)
- [Ray Dalio](people/ray-dalio/)
- [Reid Hoffman](people/reid-hoffman/)
- [René Descartes](people/rene-descartes/)
- [Richard Feynman](people/richard-feynman/)
- [Rosalind Franklin](people/rosalind-franklin/)
- [Sam Altman](people/sam-altman/)
- [Satya Nadella](people/satya-nadella/)
- [Seneca](people/seneca/)
- [Sheryl Sandberg](people/sheryl-sandberg/)
- [Simone de Beauvoir](people/simone-de-beauvoir/)
- [Socrates](people/socrates/)
- [Spinoza](people/spinoza/)
- [Srinivasa Ramanujan](people/srinivasa-ramanujan/)
- [Stephen Hawking](people/stephen-hawking/)
- [Steve Jobs](people/steve-jobs/)
- [Sun Tzu](people/sun-tzu/)
- [Theodore Roosevelt](people/theodore-roosevelt/)
- [Thomas Edison](people/thomas-edison/)
- [Thomas Kuhn](people/thomas-kuhn/)
- [Tim Cook](people/tim-cook/)
- [Tokugawa Ieyasu](people/tokugawa-ieyasu/)
- [Virginia Woolf](people/virginia-woolf/)
- [Warren Buffett](people/warren-buffett/)
- [William Shakespeare](people/william-shakespeare/)
- [Winston Churchill](people/winston-churchill/)
- [Zhuge Liang](people/zhuge-liang/)

### Fiction（架空）

- Public domain: `fiction/public-domain/`（まだなし）
- Inspired-by（現行作品）: `fiction/inspired/`（まだなし）
<!-- INDEX_JA:END -->

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
