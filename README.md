# Gitハンズオン：1枚のページをPRで提出しよう

NUTMEG（技大祭実行委員情報局）の約1時間の勉強会です。
`index.html`を編集し、Gitで変更を記録して、GitHubにPull Request（PR）を作ります。
教材も提出先もこのリポジトリにあります。

今日の完了条件は、自分のブランチでページを編集してPRを作り、`validate-submission`が成功することです。
PRのマージは行いません。Docker、Node.js、Reactも使いません。
Git、GitHubアカウント、テキストエディタ、ブラウザを用意してください。

## 始める前に

[準備ガイド](docs/setup.md)でGitのインストール、名前とメールアドレスの設定、GitHubへのログインを確認します。
WindowsのGit Bash、WSL（Ubuntu）、Macに対応しています。
GitHubからこのリポジトリへの招待が届いた場合は、先に承諾してください。

当日は最初に[Gitのアニメーション](docs/what-is-git-branch-150sec.html)を見ます。
ブランチ、手元とGitHubの違い、pushとPRの流れを約2分半で追える資料です。
主催者がブラウザで再生するので、参加者はこのページから操作を始められます。
後から自分で見る場合は、リポジトリをcloneした後にHTMLファイルをブラウザで開いてください。
GitHubのファイル画面では動画の代わりにコードが表示されます。

今回の作業は、手元でページを編集してコミットし、GitHubへpushしてPRを作る順番です。
コマンドや用語を忘れたら、[図解と用語説明](docs/concepts.md)で確かめられます。

以下のコマンドは、WindowsではGit Bash、WSLではUbuntuのターミナル、Macではターミナルに入力します。
コマンドの実行中に止まったら、次へ進まず[困ったとき](docs/troubleshooting.md)を確認してください。

## 1. リポジトリを手元に用意する

`git clone`でGitHub上の教材リポジトリを手元にコピーします。

```bash
git clone https://github.com/NUTFes/20261006-git-study.git
```

コピーしたフォルダに移動します。

```bash
cd 20261006-git-study
```

今いる場所が教材リポジトリか確認します。

```bash
git status
```

`On branch main`と表示されれば準備OKです。
cloneした直後は、共有用の`main`ブランチを見ています。
この後は、各自の変更を分けるために自分のブランチを作ります。

## 2. 自分のブランチを作る

次の`nutfes-taro`は例です。必ず自分のGitHub IDに置き換えてから実行してください。
たとえばプロフィールURLが`https://github.com/hanako`なら、`workshop/hanako`とします。

```bash
git switch -c workshop/nutfes-taro
```

今いるブランチを表示します。

```bash
git branch --show-current
```

`git switch -c`は、ブランチの作成と切り替えを一度に行います。
`git branch --show-current`に自分のブランチ名が表示されましたか？
この段階では手元にだけブランチがあり、GitHub上にはまだありません。
後でpushするとGitHub上にも作られます。
イメージを見返したいときは[ブランチの図解](docs/concepts.md#ブランチは何を分けるのか)を開いてください。

## 3. ページを編集し、表示を確認する

エディタで`index.html`を開き、次の3つの目印を自分の言葉に置き換えます。
`<title>`や`<h1>`などのHTMLタグと、`id`の値は残してください。
自動チェックがその場所を探します。

| 目印 | 書く内容 | 確認する場所 |
| --- | --- | --- |
| `CHANGE_ME_TITLE` | ページ名 | ブラウザのタブ |
| `CHANGE_ME_HEADING` | 大きな見出し | ページ上部 |
| `CHANGE_ME_MESSAGE` | 10文字以上のメッセージ | 見出しの下 |

ファイルを保存したら、ファイルマネージャーから`index.html`をダブルクリックしてブラウザで開きます。
WSLで作業している人は、Ubuntuターミナルで`explorer.exe .`を実行すると、今いるフォルダをWindowsのファイルマネージャーで開けます。
タブ、見出し、本文の3か所が変わったか確かめてください。
表示が古いままならブラウザを再読み込みします。

ページとタブが見えるように、変更後の画面をスクリーンショットで保存します。
PRを作るときに使います。
余裕があれば、既存のTailwindクラス（例：`bg-slate-100`）を変えても構いません。

## 4. 何が変わったかを確かめ、手元に記録する

Gitは、ファイルを保存しただけでは履歴を作りません。
今どこまで進んだかを確認しながら、手元の履歴に記録してみましょう。

```bash
git status --short
```

` M index.html`と表示されます。
右側の`M`はファイルを編集したこと、左側の空白はまだステージに載せていないことを表します。
ステージは、次のコミットに入れる変更を選んでおく場所です。

編集した内容を確認します。

```bash
git diff -- index.html
```

`-`で始まる行が変更前、`+`で始まる行が変更後です。
ページ名、見出し、メッセージの3か所が意図どおりか見てください。

内容が合っていたら、`index.html`をステージに載せます。

```bash
git add index.html
```

状態をもう一度見ます。

```bash
git status --short
```

`M  index.html`と出たら、左側の`M`が「ステージに載った変更」です。
通常の`git diff`はここで空になりますが、変更が消えたわけではありません。
ステージに載せた内容は、次のコマンドで見られます。

```bash
git diff --staged -- index.html
```

先ほど確認した3か所が表示されたら、コミットします。

```bash
git commit -m "Customize my workshop page"
```

`git commit`は、ステージの内容を手元の履歴に記録します。
`-m`の後ろは記録につけるメッセージです。自分の変更を表す文に書き換えても構いません。
この時点では、GitHub上のファイルはまだ変わっていません。

最後に、記録し忘れた変更がないか確かめます。

```bash
git status --short
```

何も表示されなければ、未記録の変更はありません。
別のファイルが表示された場合は、`git add .`で全部を載せず主催者に相談してください。
この課題のPRで変更するファイルは`index.html`だけです。

## 5. GitHubへ送ってPRを作る

`origin`は、clone元のGitHubリポジトリについた名前です。
pushすると、手元のコミットがGitHub上の自分のブランチに送られます。
`-u`は、手元とGitHub上の同名ブランチを対応づける指定です。

```bash
git push -u origin workshop/nutfes-taro
```

ここも`nutfes-taro`を自分のGitHub IDに置き換えます。
初回に認証画面が開いたら、GitHubアカウントでログインしてください。

pushしたら[教材リポジトリ](https://github.com/NUTFes/20261006-git-study)をブラウザで開きます。
「Compare & pull request」が見えない場合は「Pull requests」→「New pull request」から進めます。

PR画面では、取り込み先の`base`が`main`、変更元の`compare`が自分の`workshop/<GitHub ID>`か確認します。
「Files changed」には`index.html`だけが表示されていますか？
PRは「この変更を共有用のブランチへ取り込んでください」という提案です。
PRを作っても、`main`はまだ変わりません。

PR本文のテンプレートでは「変更したこと」に一文を書き、「表示確認」にチェックを入れます。
「スクリーンショット」の欄には、保存した画像をドラッグ＆ドロップしてください。
画像のアップロードが終わり、本文に`![...](https://...)`が入ってからPRを作成します。
困ったら[画像を添付する方法](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files)を見てください。

## 6. CIの結果を確認し、必要なら同じPRを直す

PRの「Checks」で`validate-submission`の結果を見ます。
CIは、決められた条件を自動で確認する仕組みです。
この課題では、変更ファイルが`index.html`だけか、HTMLの3か所を書き換えたか、PR本文に確認と画像があるかを調べます。
成功したら必須課題は完了です。

失敗した場合は、赤いチェックの「Details」を開いてエラー文を読みます。
`index.html`を直した場合は、手元の同じブランチで次の順に実行してください。

```bash
git add index.html
```

```bash
git diff --staged -- index.html
```

修正内容を確認できたら、コミットしてpushします。

```bash
git commit -m "Fix my workshop page"
git push
```

最初のpushで`-u`を指定したので、2回目からは`git push`だけで同じブランチに送れます。
新しいコミットは既存のPRに追加され、CIも再実行されます。
新しいPRを作る必要はありません。

PR本文だけを直した場合は、GitHub上で本文を編集して保存します。
この場合は手元でコミットする必要はありません。
PRの更新方法は[図解と用語説明](docs/concepts.md#prとgit-pullは別の操作)でも確認できます。

## 早く終わった人へ

[Gitの追加課題](docs/advanced-git.md)で、状態、差分、履歴を読み、`git restore --staged`と`git stash`を練習できます。提出PRが成功してから取り組んでください。練習用のファイルはコミットもpushもしません。

## 当日の時間配分

| 時間 | 内容 |
| --- | --- |
| 0〜10分 | [アニメーションを見て、今回の課題との違いを確認](docs/lecture.md) |
| 10〜17分 | 環境確認、clone、ブランチ作成 |
| 17〜30分 | HTML編集、表示確認、スクリーンショット |
| 30〜40分 | 差分確認、ステージ、コミット、push |
| 40〜55分 | PR作成、CIの指摘を修正 |
| 55〜60分 | 結果確認と振り返り。早く終わった人は追加課題へ |

今回はコンフリクト解消とDockerを必須課題に含めません。
「編集、確認、記録、共有、PR、CI」を一度通してみましょう。
ページの見た目には学習用の[Tailwind Play CDN](https://tailwindcss.com/docs/installation/play-cdn)を使うため、正しく表示するにはインターネット接続が必要です。
