# Gitハンズオン：1枚のページをPRで提出しよう

NUTMEG（技大祭実行委員情報局）の約1時間の勉強会です。`index.html`を編集し、Gitで変更を記録して、GitHubにPull Request（PR）を作ります。教材も提出先もこのリポジトリにあります。

今日のゴールは、自分のブランチでページを編集し、表示を確かめてPRを作り、`validate-submission`が成功することです。PRのマージは行いません。Docker、Node.js、Reactは使いません。必要なのはGit、GitHubアカウント、テキストエディタ、ブラウザです。

先に[準備ガイド](docs/setup.md)でGitの設定と書き込み権限を確認してください。WindowsのGit Bash、WSL（Ubuntu）、Macの手順を用意しています。用語や操作の関係が分からなくなったら、[図解と用語説明](docs/concepts.md)を開いてください。

## 今日の進め方

### 1. リポジトリを取得して、自分のブランチを作る

WindowsはGit Bash、WSLはUbuntuのターミナル、Macはターミナルで操作します。`<GitHub ID>`は自分のIDに置き換え、`<`と`>`は入力しません。GitHub IDが`nutfes-taro`なら、ブランチ名は`workshop/nutfes-taro`です。

```bash
git clone https://github.com/NUTFes/20261006-git-study.git
cd 20261006-git-study
git switch -c workshop/<GitHub ID>
git branch --show-current
```

最後のコマンドで自分のブランチ名が表示されれば準備完了です。ブランチは同じ変更履歴から分かれた作業の系列です。全員が同じ`index.html`を編集するため、共有の`main`から各自のブランチを作ります。

### 2. ページを編集して、ブラウザで確かめる

`index.html`をエディタで開き、次の3つの目印を自分の言葉に置き換えます。`<title>`や`<h1>`などのHTMLタグと、`id`の値は残してください。自動チェックがその場所を探します。

| 目印 | 入れる内容の例 |
| --- | --- |
| `CHANGE_ME_TITLE` | ブラウザのタブに表示するページ名 |
| `CHANGE_ME_HEADING` | ページ内の大きな見出し |
| `CHANGE_ME_MESSAGE` | 10文字以上のメッセージ |

保存したら、ファイルマネージャーから`index.html`をダブルクリックしてブラウザで開きます。ページ名、見出し、本文が変わり、`CHANGE_ME_`が残っていないことを確認してください。表示結果のスクリーンショットも撮ってください。余裕があれば、既存のTailwindクラス（例：`bg-slate-100`）を変えても構いません。

### 3. 変更を確認して、コミットする

```bash
git status --short
git diff -- index.html
git add index.html
git status --short
git commit -m "Update my workshop page"
```

最初の`git status --short`では` M index.html`と表示されます。左側の空白は「まだステージに載せていない変更」を表します。`git diff`では、編集前と編集後の行を確認します。`git add`の後は`M  index.html`となり、変更がステージに載ったことが分かります。ステージは、次のコミットに含める変更を選ぶ場所です。`git commit`で、その内容を手元の履歴に記録します。メッセージは自分の変更内容に合わせて書き換えて構いません。

もし別のファイルも変更されていたら、そのファイルを`git add`する前に主催者へ相談してください。この課題のPRで変更するファイルは`index.html`だけです。

### 4. GitHubへpushして、PRを作る

```bash
git push -u origin workshop/<GitHub ID>
```

`origin`は取得元のGitHubリポジトリについた名前です。pushすると、手元のコミットがGitHub上の自分のブランチへ送られます。初回の認証画面が開いたら、GitHubアカウントでログインします。

[教材リポジトリ](https://github.com/NUTFes/20261006-git-study)をブラウザで開き、表示される「Compare & pull request」からPRを作ります。取り込み先が`main`、変更元が自分の`workshop/<GitHub ID>`になっているか確認してください。テンプレートの「変更したこと」に一文を書き、「表示確認」にチェックを入れ、「スクリーンショット」の欄に画像をドラッグ＆ドロップします。画像を貼る方法は[GitHubの説明](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files)も参照できます。

PRは変更を取り込んでもらうための提案です。PRを作った時点では`main`のページは変わりません。

### 5. 自動チェックの結果を見る

PRの「Checks」で`validate-submission`の結果を確認します。CIは、提出内容を自動で確認する仕組みです。この課題では、変更したファイル、HTMLの3か所、PR本文のチェックとスクリーンショットを確認します。成功したら今日の課題は完了です。

失敗したら、エラー文を読んで修正します。`index.html`を直した場合は、同じブランチで次のコマンドを実行してください。既存のPRが自動で更新されます。新しいPRを作る必要はありません。

```bash
git add index.html
git commit -m "Fix my workshop page"
git push
```

PR本文だけを直した場合は、GitHub上のPR本文を編集して保存します。CIが再実行されるので、結果を確認してください。困ったときは[トラブルシューティング](docs/troubleshooting.md)を見てください。

## 早く終わった人へ

[Gitの追加課題](docs/advanced-git.md)では、`git status`で今の状態を読み、差分と履歴を確認し、`git restore --staged`と`git stash`を試します。練習用のファイルを手元だけで使うため、提出PRのチェックには影響しません。必須課題が終わってから取り組んでください。

## 当日の時間配分

| 時間 | 内容 |
| --- | --- |
| 0〜10分 | [GitとPRの流れ](docs/lecture.md)を説明 |
| 10〜17分 | 環境確認、clone、ブランチ作成 |
| 17〜30分 | HTML編集、表示確認、スクリーンショット |
| 30〜40分 | 差分確認、コミット、push |
| 40〜55分 | PR作成、CIの指摘を修正 |
| 55〜60分 | 結果確認と振り返り。早く終わった人は追加課題へ |

今回はコンフリクト解消とDockerを必須課題に含めません。まず、開発で繰り返す「編集、確認、記録、共有、PR、CI」の流れを一度通します。ページの表示には学習用の[Tailwind Play CDN](https://tailwindcss.com/docs/installation/play-cdn)を使うため、見た目を正しく表示するにはインターネット接続が必要です。
