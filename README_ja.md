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

**ビルダー / ビジネス**
- [Andy Grove](people/andy-grove/)
- [Bill Gates](people/bill-gates/)
- [Charlie Munger](people/charlie-munger/)
- [Elon Musk](people/elon-musk/)
- [Howard Schultz](people/howard-schultz/)
- [Indra Nooyi](people/indra-nooyi/)
- [Jack Ma](people/jack-ma/)
- [Jack Welch](people/jack-welch/)
- [Jeff Bezos](people/jeff-bezos/)
- [Jensen Huang](people/jensen-huang/)
- [Marc Andreessen](people/marc-andreessen/)
- [Mary Barra](people/mary-barra/)
- [Masayoshi Son](people/masayoshi-son/)
- [Oprah Winfrey](people/oprah-winfrey/)
- [Paul Graham](people/paul-graham/)
- [Peter Thiel](people/peter-thiel/)
- [Pony Ma](people/pony-ma/)
- [Ray Dalio](people/ray-dalio/)
- [Reid Hoffman](people/reid-hoffman/)
- [Sam Altman](people/sam-altman/)
- [Satya Nadella](people/satya-nadella/)
- [Sheryl Sandberg](people/sheryl-sandberg/)
- [Steve Jobs](people/steve-jobs/)
- [Tim Cook](people/tim-cook/)
- [Warren Buffett](people/warren-buffett/)

**政治 / 統治**
- [Abraham Lincoln](people/abraham-lincoln/)
- [Angela Merkel](people/angela-merkel/)
- [Augustus](people/augustus/)
- [Cardinal Richelieu](people/cardinal-richelieu/)
- [Catherine the Great](people/catherine-the-great/)
- [Charles-Maurice de Talleyrand](people/talleyrand/)
- [Franklin D. Roosevelt](people/franklin-d-roosevelt/)
- [Harry Hopkins](people/harry-hopkins/)
- [Julius Caesar](people/julius-caesar/)
- [Lee Kuan Yew](people/lee-kuan-yew/)
- [Mahatma Gandhi](people/mahatma-gandhi/)
- [Margaret Thatcher](people/margaret-thatcher/)
- [Nelson Mandela](people/nelson-mandela/)
- [Otto von Bismarck](people/otto-von-bismarck/)
- [Queen Elizabeth I](people/queen-elizabeth-i/)
- [Sokollu Mehmed Pasha](people/sokollu-mehmed-pasha/)
- [Theodore Roosevelt](people/theodore-roosevelt/)
- [Thomas Cromwell](people/thomas-cromwell/)
- [Tokugawa Ieyasu](people/tokugawa-ieyasu/)
- [Toyotomi Hidenaga](people/toyotomi-hidenaga/)
- [Winston Churchill](people/winston-churchill/)

**軍略 / 戦略**
- [Alexander the Great](people/alexander-the-great/)
- [Carl von Clausewitz](people/carl-von-clausewitz/)
- [George C. Marshall](people/george-c-marshall/)
- [Hannibal](people/hannibal/)
- [Kuroda Kanbei](people/kuroda-kanbei/)
- [Marcus Agrippa](people/marcus-agrippa/)
- [Miyamoto Musashi](people/miyamoto-musashi/)
- [Napoleon Bonaparte](people/napoleon-bonaparte/)
- [Oda Nobunaga](people/oda-nobunaga/)
- [Sun Tzu](people/sun-tzu/)
- [Zhuge Liang](people/zhuge-liang/)

**哲学**
- [Aristotle](people/aristotle/)
- [Confucius](people/confucius/)
- [David Hume](people/david-hume/)
- [Derek Parfit](people/derek-parfit/)
- [Epictetus](people/epictetus/)
- [Friedrich Nietzsche](people/friedrich-nietzsche/)
- [Hannah Arendt](people/hannah-arendt/)
- [Immanuel Kant](people/immanuel-kant/)
- [John Rawls](people/john-rawls/)
- [John Stuart Mill](people/john-stuart-mill/)
- [Karl Popper](people/karl-popper/)
- [Kierkegaard](people/kierkegaard/)
- [Ludwig Wittgenstein](people/ludwig-wittgenstein/)
- [Marcus Aurelius](people/marcus-aurelius/)
- [Michel Foucault](people/michel-foucault/)
- [Plato](people/plato/)
- [René Descartes](people/rene-descartes/)
- [Seneca](people/seneca/)
- [Simone de Beauvoir](people/simone-de-beauvoir/)
- [Socrates](people/socrates/)
- [Spinoza](people/spinoza/)
- [Thomas Kuhn](people/thomas-kuhn/)

**科学 / 数学**
- [Ada Lovelace](people/ada-lovelace/)
- [Albert Einstein](people/albert-einstein/)
- [Barbara McClintock](people/barbara-mcclintock/)
- [Carl Sagan](people/carl-sagan/)
- [Charles Darwin](people/charles-darwin/)
- [Donald Knuth](people/donald-knuth/)
- [Emmy Noether](people/emmy-noether/)
- [Galileo Galilei](people/galileo-galilei/)
- [Isaac Newton](people/isaac-newton/)
- [James Clerk Maxwell](people/james-clerk-maxwell/)
- [John von Neumann](people/john-von-neumann/)
- [Leonardo da Vinci](people/leonardo-da-vinci/)
- [Marie Curie](people/marie-curie/)
- [Max Planck](people/max-planck/)
- [Michael Faraday](people/michael-faraday/)
- [Niels Bohr](people/niels-bohr/)
- [Nikola Tesla](people/nikola-tesla/)
- [Richard Feynman](people/richard-feynman/)
- [Rosalind Franklin](people/rosalind-franklin/)
- [Srinivasa Ramanujan](people/srinivasa-ramanujan/)
- [Stephen Hawking](people/stephen-hawking/)
- [Thomas Edison](people/thomas-edison/)
- [Vannevar Bush](people/vannevar-bush/)

**計算機 / ソフトウェア**
- [Alan Kay](people/alan-kay/)
- [Alan Turing](people/alan-turing/)
- [Bjarne Stroustrup](people/bjarne-stroustrup/)
- [Brendan Eich](people/brendan-eich/)
- [Claude Shannon](people/claude-shannon/)
- [Dennis Ritchie](people/dennis-ritchie/)
- [Grace Hopper](people/grace-hopper/)
- [Guido van Rossum](people/guido-van-rossum/)
- [James Gosling](people/james-gosling/)
- [John Carmack](people/john-carmack/)
- [Ken Thompson](people/ken-thompson/)
- [Linus Torvalds](people/linus-torvalds/)
- [Margaret Hamilton](people/margaret-hamilton/)

**経済 / 社会科学**
- [Adam Smith](people/adam-smith/)
- [Amos Tversky](people/amos-tversky/)
- [Daniel Kahneman](people/daniel-kahneman/)
- [Elinor Ostrom](people/elinor-ostrom/)
- [Herbert A. Simon](people/herbert-a-simon/)
- [Jean-Baptiste Colbert](people/jean-baptiste-colbert/)
- [John Maynard Keynes](people/john-maynard-keynes/)
- [Milton Friedman](people/milton-friedman/)

**芸術 / 文学**
- [Fyodor Dostoevsky](people/fyodor-dostoevsky/)
- [Haruki Murakami](people/haruki-murakami/)
- [James Joyce](people/james-joyce/)
- [Jane Austen](people/jane-austen/)
- [Leo Tolstoy](people/leo-tolstoy/)
- [Virginia Woolf](people/virginia-woolf/)
- [William Shakespeare](people/william-shakespeare/)

### 助手 / 相棒

- [Cardinal Richelieu](people/cardinal-richelieu/)
- [Charles-Maurice de Talleyrand](people/talleyrand/)
- [Detective With a Heart (Inspired)](fiction/inspired/detective-with-heart/)
- [Dr. John Seward](fiction/public-domain/john-seward/)
- [Dr. John Watson](fiction/public-domain/john-watson/)
- [Eccentric Genius Inventor (Inspired)](fiction/inspired/eccentric-genius-inventor/)
- [Faithful Companion (Archetype)](fiction/inspired/samwise-archetype/)
- [Gentle Healer / Logistics Lead (Inspired)](fiction/inspired/gentle-healer-logistics/)
- [George C. Marshall](people/george-c-marshall/)
- [Harry Hopkins](people/harry-hopkins/)
- [Horatio](fiction/public-domain/horatio/)
- [Idol Producer / Coach (Inspired)](fiction/inspired/idol-producer-coach/)
- [Jean-Baptiste Colbert](people/jean-baptiste-colbert/)
- [Kuroda Kanbei](people/kuroda-kanbei/)
- [Magic Academy Professor (Inspired)](fiction/inspired/magic-academy-professor/)
- [Marcus Agrippa](people/marcus-agrippa/)
- [Mecha Operations Tactician (Inspired)](fiction/inspired/mecha-operations-tactician/)
- [Mina Harker](fiction/public-domain/mina-harker/)
- [Quiet Samurai Mentor (Inspired)](fiction/inspired/quiet-samurai-mentor/)
- [Sancho Panza](fiction/public-domain/sancho-panza/)
- [Shōgi Master Strategist (Inspired)](fiction/inspired/shogi-master-strategist/)
- [Sokollu Mehmed Pasha](people/sokollu-mehmed-pasha/)
- [Streetwise Fixer (Inspired)](fiction/inspired/streetwise-fixer/)
- [Thomas Cromwell](people/thomas-cromwell/)
- [Toyotomi Hidenaga](people/toyotomi-hidenaga/)
- [Tsundere Analyst (Inspired)](fiction/inspired/tsundere-analyst/)
- [Vannevar Bush](people/vannevar-bush/)
- [Virgil (Dante’s guide)](fiction/public-domain/virgil/)
- [Zhuge Liang](people/zhuge-liang/)

### Fiction（架空）

**Public domain**
- *comedy*
  - [Sancho Panza](fiction/public-domain/sancho-panza/)
- *drama*
  - [Dorian Gray](fiction/public-domain/dorian-gray/)
  - [Ebenezer Scrooge](fiction/public-domain/ebenezer-scrooge/)
  - [Friday](fiction/public-domain/friday/)
  - [Horatio](fiction/public-domain/horatio/)
  - [Patroclus](fiction/public-domain/patroclus/)
- *fantasy*
  - [Alice](fiction/public-domain/alice/)
  - [Virgil (Dante’s guide)](fiction/public-domain/virgil/)
- *horror*
  - [Count Dracula](fiction/public-domain/dracula/)
  - [Dr. John Seward](fiction/public-domain/john-seward/)
  - [Mina Harker](fiction/public-domain/mina-harker/)
  - [Professor Abraham Van Helsing](fiction/public-domain/abraham-van-helsing/)
- *mystery*
  - [Dr. John Watson](fiction/public-domain/john-watson/)
  - [Sherlock Holmes](fiction/public-domain/sherlock-holmes/)
- *scifi*
  - [Frankenstein’s Creature](fiction/public-domain/frankensteins-creature/)
  - [Victor Frankenstein](fiction/public-domain/frankenstein/)

**Inspired-by（現行作品）**
- *drama*
  - [Idol Producer / Coach (Inspired)](fiction/inspired/idol-producer-coach/)
  - [Streetwise Fixer (Inspired)](fiction/inspired/streetwise-fixer/)
- *fantasy*
  - [Faithful Companion (Archetype)](fiction/inspired/samwise-archetype/)
  - [Gentle Healer / Logistics Lead (Inspired)](fiction/inspired/gentle-healer-logistics/)
  - [Magic Academy Professor (Inspired)](fiction/inspired/magic-academy-professor/)
- *mystery*
  - [Detective With a Heart (Inspired)](fiction/inspired/detective-with-heart/)
- *other*
  - [Quiet Samurai Mentor (Inspired)](fiction/inspired/quiet-samurai-mentor/)
  - [Shōgi Master Strategist (Inspired)](fiction/inspired/shogi-master-strategist/)
  - [Shōnen Determination Hero (Inspired)](fiction/inspired/shonen-determination-hero/)
  - [Tsundere Analyst (Inspired)](fiction/inspired/tsundere-analyst/)
- *scifi*
  - [Cyberpunk Hacker-Detective (Inspired)](fiction/inspired/cyberpunk-hacker-detective/)
  - [Eccentric Genius Inventor (Inspired)](fiction/inspired/eccentric-genius-inventor/)
  - [Mecha Operations Tactician (Inspired)](fiction/inspired/mecha-operations-tactician/)
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
