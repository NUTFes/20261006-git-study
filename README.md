# Gitハンズオン：1枚のページをPRで提出しよう

NUTMEG（技大祭実行委員情報局）の約1時間の勉強会です。`index.html`を編集し、Gitで変更を記録して、GitHubにPull Request（PR）を作ります。教材も提出先もこのリポジトリにあります。

今日の完了条件は、自分のブランチでページを編集してPRを作り、`validate-submission`が成功することです。PRのマージは行いません。Docker、Node.js、Reactは使いません。Git、GitHubアカウント、テキストエディタ、ブラウザを用意してください。

## 始める前に

[準備ガイド](docs/setup.md)でGitのインストール、名前とメールアドレスの設定、GitHubへのログインを確認します。WindowsのGit Bash、WSL（Ubuntu）、Macに対応しています。GitHubからこのリポジトリへの招待が届いた場合は、先に承諾してください。

Gitは、ファイルの変更を履歴として記録する道具です。GitHubは、その履歴をほかの人と共有し、PRを作るサービスです。今回の作業は、手元で編集・記録してからGitHubへ送る順番で進みます。初めての人は、操作を始める前に[図で見るGitとGitHub](docs/concepts.md)の「全体の流れ」まで読んでください。

以下のコマンドは、WindowsではGit Bash、WSLではUbuntuのターミナル、Macではターミナルに入力します。コマンドの実行中に止まったら、次へ進まず[困ったとき](docs/troubleshooting.md)を確認してください。

## 1. リポジトリを手元に用意する

`git clone`はGitHub上の教材リポジトリを手元へコピーします。続く`cd`は、コピーしたフォルダに移動します。`cd`を忘れると、後のGitコマンドは別の場所で実行されます。

```bash
git clone https://github.com/NUTFes/20261006-git-study.git
cd 20261006-git-study
git status
```

`git status`に`On branch main`と表示されれば、教材リポジトリ内にいます。cloneした直後は`main`という共有用のブランチを見ています。ブランチは、一つの履歴から分かれて作業を続けるための名前です。各自の変更を分けるため、次に自分のブランチを作ります。

## 2. 自分のブランチを作る

次の`nutfes-taro`は例です。必ず自分のGitHub IDに置き換えてから実行してください。たとえばGitHubのプロフィールURLが`https://github.com/hanako`なら、`workshop/hanako`とします。

```bash
git switch -c workshop/nutfes-taro
git branch --show-current
```

`git switch -c`は、ブランチの作成と切り替えを一度に行います。2行目に自分のブランチ名が表示されたことを確認してください。この操作だけでは、GitHub上に自分のブランチはまだありません。後でpushすると作られます。[ブランチの図解](docs/concepts.md#ブランチは何を分けるのか)も参照できます。

## 3. ページを編集し、表示を確認する

エディタで`index.html`を開き、次の目印を自分の言葉に置き換えます。`<title>`や`<h1>`などのHTMLタグと、`id`の値は残してください。自動チェックがその場所を探します。

| 目印 | 書く内容 | 確認する場所 |
| --- | --- | --- |
| `CHANGE_ME_TITLE` | ページ名 | ブラウザのタブ |
| `CHANGE_ME_HEADING` | 大きな見出し | ページ上部 |
| `CHANGE_ME_MESSAGE` | 10文字以上のメッセージ | 見出しの下 |

ファイルを保存し、ファイルマネージャーから`index.html`をダブルクリックしてブラウザで開きます。タブ、見出し、本文を見て、3か所とも変わったことを確認してください。表示が古いままならブラウザを再読み込みします。変更後のブラウザ画面を、ページとタブが分かるようにスクリーンショットで保存します。余裕があれば、既存のTailwindクラス（例：`bg-slate-100`）を変えても構いません。

## 4. 何が変わったかを確かめ、手元に記録する

Gitは、ファイルを保存しただけでは履歴を作りません。まず変更したファイルと内容を確認し、コミットに入れる変更を`git add`で選びます。

```bash
git status --short
git diff -- index.html
git add index.html
git status --short
git diff --staged -- index.html
git commit -m "Customize my workshop page"
git status --short
```

最初の`git status --short`には` M index.html`が表示されます。左側が空白、右側が`M`なので、変更は手元のファイルにあり、まだステージに載っていません。`git diff`では`-`で始まる行が変更前、`+`で始まる行が変更後です。3か所が意図どおりか読んでください。

`git add index.html`で、現在の`index.html`の変更を次のコミットの候補であるステージに載せます。次の`git status --short`は`M  index.html`となり、今度は左側に`M`が表示されます。通常の`git diff`はここで空になります。ステージに載った内容は`git diff --staged -- index.html`で確認できます。

`git commit`はステージの内容を手元の履歴に記録します。`-m`の後ろの文は、その記録を後から見分けるためのメッセージです。自分の変更を表す文に書き換えても構いません。最後の`git status --short`が空なら、未記録の変更はありません。ここまでの操作では、GitHub上のファイルはまだ変わっていません。

この課題のPRで変更するファイルは`index.html`だけです。`git status`に別のファイルも表示された場合は、`git add .`で全部を載せず、主催者に相談してください。

## 5. GitHubへ送ってPRを作る

`origin`は、clone元のGitHubリポジトリについた名前です。pushすると、手元で記録したコミットがGitHub上の自分のブランチに送られます。`-u`は、手元とGitHub上の同名ブランチを対応づける指定です。

```bash
git push -u origin workshop/nutfes-taro
```

ここも`nutfes-taro`を自分のGitHub IDに置き換えます。初回に認証画面が開いたら、GitHubアカウントでログインしてください。push後に[教材リポジトリ](https://github.com/NUTFes/20261006-git-study)をブラウザで開きます。「Compare & pull request」が見えない場合は「Pull requests」→「New pull request」から進めます。

PR画面では、取り込み先の`base`が`main`、変更元の`compare`が自分の`workshop/<GitHub ID>`か確認します。「Files changed」に`index.html`だけが表示されていることも確認してください。PRは「この変更を共有用のブランチへ取り込んでください」という提案です。PRを作っても、`main`はまだ変わりません。

PR本文のテンプレートでは「変更したこと」に一文を書き、「表示確認」にチェックを入れ、「スクリーンショット」の欄に保存した画像をドラッグ＆ドロップします。画像のアップロードが終わり、本文に`![...](https://...)`が入ってからPRを作成してください。[画像を添付する方法](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files)も参照できます。

## 6. CIの結果を確認し、必要なら同じPRを直す

PRの「Checks」で`validate-submission`を確認します。CIは、決められた条件を自動で確認する仕組みです。この課題では、変更ファイルが`index.html`だけか、HTMLの3か所を書き換えたか、PR本文に確認と画像があるかを調べます。成功したら必須課題は完了です。

失敗した場合は、赤いチェックの「Details」を開き、表示されたエラー文を読みます。`index.html`を直した場合は、手元の同じブランチで次を実行してください。

```bash
git add index.html
git diff --staged -- index.html
git commit -m "Fix my workshop page"
git push
```

最初のpushで`-u`を指定したので、2回目からは`git push`だけで同じブランチに送れます。新しいコミットは既存のPRに追加され、CIも再実行されます。PR本文だけを直した場合は、GitHub上で本文を編集して保存します。この場合は手元でコミットする必要はありません。PRの更新方法は[図解と用語説明](docs/concepts.md#prとgit-pullは別の操作)でも確認できます。

## 早く終わった人へ

[Gitの追加課題](docs/advanced-git.md)で、状態、差分、履歴を読み、`git restore --staged`と`git stash`を練習できます。提出PRが成功してから取り組んでください。練習用のファイルはコミットもpushもしません。

## 当日の時間配分

| 時間 | 内容 |
| --- | --- |
| 0〜10分 | [GitとGitHubの流れ](docs/lecture.md)を説明 |
| 10〜17分 | 環境確認、clone、ブランチ作成 |
| 17〜30分 | HTML編集、表示確認、スクリーンショット |
| 30〜40分 | 差分確認、ステージ、コミット、push |
| 40〜55分 | PR作成、CIの指摘を修正 |
| 55〜60分 | 結果確認と振り返り。早く終わった人は追加課題へ |

今回はコンフリクト解消とDockerを必須課題に含めません。まず「編集、確認、記録、共有、PR、CI」を一度通します。ページの見た目には学習用の[Tailwind Play CDN](https://tailwindcss.com/docs/installation/play-cdn)を使うため、正しく表示するにはインターネット接続が必要です。
