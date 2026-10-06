# Gitハンズオン：自己紹介ページをPRで提出しよう

NUTMEG（技大祭実行委員情報局）の約1時間の勉強会です。
最初の15分はGitのアニメーションを見て、残り45分で実際に手を動かします。

今日のゴールは、自己紹介ページを3回に分けて編集・コミットし、GitHubにPull Request（PR）を作ることです。
PRの`validate-submission`が成功したら完了です。
PRのマージは行いません。

## 始める前に

[準備ガイド](docs/setup.md)で、Gitのインストールと設定、GitHubへのログインを確認してください。
WindowsのGit Bash、WSL（Ubuntu）、Macに対応しています。
リポジトリへの招待が届いていたら承諾してください。

当日は主催者が[Gitのアニメーション](docs/what-is-git-branch-150sec.html)をブラウザで再生し、質問を受けます。
GitHub上でHTMLを開くとコードが表示されるため、自分で再生するときはファイルをダウンロードしてブラウザで開いてください。

ハンズオンでは、ページ名、見出し、自己紹介文を**1か所ずつ編集してコミット**します。
その後、まとめてpushしてPRを作ります。
コマンドはGit Bash、WSLのUbuntuターミナル、Macのターミナルに入力してください。
途中で止まったら[困ったとき](docs/troubleshooting.md)を確認します。

## 1. リポジトリを手元に用意する

`git clone`で、GitHub上の教材を自分のパソコンにコピーします。

```bash
git clone https://github.com/NUTFes/20261006-git-study.git
```

コピーしたフォルダへ移動します。

```bash
cd 20261006-git-study
```

今いる場所とブランチを確かめます。

```bash
git status
```

`On branch main`と表示されれば準備OKです。`main`は、みんなで共有するためのブランチです。

## 2. 自分のブランチを作る

自分の作業を`main`と分けるために、ブランチを作ります。
コマンド内の`nutfes-taro`は例です。必ず自分のGitHub IDに置き換えてください。
プロフィールURLが`https://github.com/hanako`なら、ブランチ名は`feat/hanako`です。

```bash
git switch -c feat/nutfes-taro
```

今いるブランチを表示します。

```bash
git branch --show-current
```

自分の`feat/<GitHub ID>`が表示されましたか？
`git switch -c`は、ブランチの作成と切り替えを一度に行います。
この段階ではブランチは手元だけにあり、pushするとGitHub上にも作られます。

ブランチ名のルールは開発プロジェクトごとに異なります。今回は`feat/<GitHub ID>`を使います。

<details>
<summary>ほかのブランチ名の例を見る</summary>

- `feat/hanako`、`feature/hanako`：機能を追加するとき
- `fix/login-error`：不具合を直すとき
- `docs/setup-guide`：説明文を直すとき
- `chore/dependency-update`：設定や依存関係を整理するとき

実際の開発では、そのプロジェクトの決まりに合わせてください。

</details>

## 3. ページ名を変えて、1回目のコミットを作る

このリポジトリは公開されています。自己紹介には実名や連絡先を書かず、NUTMEGで使う名前を使ってください。

エディタで`index.html`を開き、「1. ブラウザのタブに表示するページ名を変えよう」のコメントを探します。
その下にある`CHANGE_ME_TITLE`をページ名に変えてください。たとえば`<title>たろうの自己紹介</title>`です。
`<title>`タグは残し、中の文字だけを変えて保存します。ページ名はブラウザのタブに表示されます。

まず、編集したファイルを確認します。

```bash
git status --short
```

` M index.html`と表示されます。右側の`M`は編集した印です。

次に、変更した行を見ます。

```bash
git diff -- index.html
```

`-`で始まる行が変更前、`+`で始まる行が変更後です。ページ名だけが変わっているか確かめてください。

この変更を次のコミットに入れるため、ステージに載せます。

```bash
git add index.html
```

ステージは、次のコミットに記録する変更を選んでおく場所です。選んだ内容を確認します。

```bash
git diff --staged -- index.html
```

ページ名の変更が表示されたら、1回目のコミットを作ります。

```bash
git commit -m "feat: ページのタイトルを変更"
```

コミットは、変更を手元の履歴に記録します。この時点では、GitHub上のページはまだ変わっていません。

コミットメッセージの書き方もプロジェクトごとに異なります。今回の例では、`feat:`の後ろに日本語で変更内容を書きます。

<details>
<summary>コミットメッセージのほかの書き方を見る</summary>

`feat:`は機能追加、`fix:`は修正、`docs:`は文章の変更を表す例です。
関連するIssueがあるプロジェクトでは、番号を添えることもあります。
以下は、次の変更をステージに載せた後に使う書き方の例です。今は実行しなくて大丈夫です。

```bash
git commit -m "feat: #123 自己紹介文を追加"
```

理由を補足したいときは、最初の`"`を閉じずに改行できます。
件名の次に空行を入れ、本文を書いてから最後の`"`を閉じます。
入力中に`>`などの続きの入力待ちが表示されても、最後の`"`まで入力すれば実行されます。

```bash
git commit -m "feat: 自己紹介文を追加

好きなことと、勉強会で挑戦したいことを書いた"
```

今回は短い1行のメッセージで十分です。

</details>

## 4. 見出しを変えて、2回目のコミットを作る

`index.html`で「2. カードの見出しを変えよう」のコメントを探します。
その下にある`CHANGE_ME_HEADING`を、自分の名前が分かる見出しに変えてください。たとえば「たろうです！」です。
`<h1>`タグ、`id`、`class`は残し、タグの間の文字だけを変えて保存します。

見出しだけが変わったか確認します。

```bash
git diff -- index.html
```

確認した変更をステージに載せます。

```bash
git add index.html
```

コミットに入る内容をもう一度見ます。

```bash
git diff --staged -- index.html
```

見出しの変更だけなら、2回目のコミットを作ります。

```bash
git commit -m "feat: 自己紹介の見出しを追加"
```

## 5. 自己紹介文を変えて、3回目のコミットを作る

`index.html`で「3. 自己紹介の文章を変えよう」のコメントを探します。
その下にある`CHANGE_ME_MESSAGE`を、10文字以上の自己紹介文に変えてください。
たとえば「ゲーム作りに興味があります。今日はGitを覚えたいです！」のように、好きなことや挑戦したいことを書きます。

必須課題では`<p>`タグ、`id`、`class`を残し、タグの間の文章だけを変えます。
リストなどのHTMLを追加する必要はありません。
余裕があれば、既存のTailwindクラスを変えて色や余白を試しても構いません。

文章の変更だけか確認します。

```bash
git diff -- index.html
```

変更をステージに載せます。

```bash
git add index.html
```

3回目のコミットに入る内容を確認します。

```bash
git diff --staged -- index.html
```

自己紹介文の変更が表示されたら、コミットします。

```bash
git commit -m "feat: 自己紹介文を追加"
```

保存した`index.html`をファイルマネージャーからダブルクリックし、ブラウザで開きます。
WSLで作業している人は、Ubuntuターミナルで次を実行するとWindowsのファイルマネージャーが開きます。

```bash
explorer.exe .
```

ブラウザのタブ、カードの見出し、自己紹介文が変わっているか確認してください。
古い表示のままなら再読み込みします。
ページとタブが写るスクリーンショットを撮って保存します。
画像は後でPR本文に添付するため、リポジトリに入れないでください。

最後に、未記録の変更が残っていないか確かめます。

```bash
git status --short
```

何も表示されなければOKです。別のファイルが表示されたら、`git add .`で全部を載せず主催者に相談してください。

## 6. GitHubへpushしてPRを作る

3回のコミットは、まだ自分のパソコンの中にあります。
pushしてGitHub上の自分のブランチへ送ります。
`nutfes-taro`は、自分のGitHub IDに置き換えてください。

```bash
git push -u origin feat/nutfes-taro
```

`origin`はclone元のリポジトリの名前です。
`-u`を付けると、手元のブランチとGitHub上のブランチが対応づけられます。
認証画面が開いたら、GitHubアカウントでログインしてください。

[教材リポジトリ](https://github.com/NUTFes/20261006-git-study)をブラウザで開き、「Compare & pull request」へ進みます。
見つからなければ「Pull requests」→「New pull request」から作れます。

取り込み先の`base`が`main`、変更元の`compare`が自分の`feat/<GitHub ID>`か確認してください。
「Files changed」には`index.html`だけが表示されるはずです。
PRは、変更を共有ブランチへ取り込んでもらうための提案です。PRを作った時点では`main`は変わりません。

PR本文のテンプレートでは「変更したこと」に一文を書き、「表示確認」にチェックを入れます。
「スクリーンショット」の欄に先ほどの画像をドラッグ＆ドロップし、アップロードが終わってからPRを作成してください。
画像を入れにくい場合は[GitHubの添付方法](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files)を確認します。

## 7. CIを確認し、必要なら同じPRを直す

PRの「Checks」で`validate-submission`の結果を見ます。CIは提出内容を自動で確認します。
今回調べるのは、変更ファイルが`index.html`だけか、3か所の文章を書き換えたか、PR本文の確認と画像があるかです。
3回のコミット数やメッセージの形式は自動チェックしません。

失敗した場合は赤いチェックの「Details」を開き、エラー文を読みます。`index.html`を直したら、同じブランチで次の順に実行してください。

```bash
git add index.html
```

```bash
git diff --staged -- index.html
```

修正した内容が合っていれば、コミットしてpushします。

```bash
git commit -m "fix: 自己紹介ページを修正"
```

```bash
git push
```

新しいコミットは既存のPRに追加され、CIも再実行されます。PRを作り直す必要はありません。
PR本文だけを直した場合は、GitHub上で本文を編集して保存します。手元でのコミットは不要です。

## 早く終わった人へ

[Gitの追加課題](docs/advanced-git.md)で、`git status`、`git diff`、履歴、`git restore --staged`、`git stash`を試せます。
提出PRが成功してから、できるところまで進めてください。練習用ファイルはコミットもpushもしません。
