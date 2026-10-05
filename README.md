# Git ハンズオン：1枚のページを PR で提出しよう

NUTMEG（技大祭実行委員情報局）の約1時間の勉強会です。`index.html` を少し編集し、Git で変更を記録して GitHub に Pull Request（PR）を作ります。教材と提出先はこのリポジトリです。

## 今日のゴール

- 自分のブランチで `index.html` の3か所を編集し、ブラウザで表示を確認する。
- 変更をコミットして push し、表示結果のスクリーンショットを添えた PR を作る。
- PR の **validate-submission** が成功する。これで勉強会の課題は完了です。PR のマージは行いません。

Docker・Node.js・React は使いません。必要なのは Git、GitHub アカウント、テキストエディタ、ブラウザです。ページの見た目には学習用の [Tailwind Play CDN](https://tailwindcss.com/docs/installation/play-cdn) を使うため、表示時はインターネット接続が必要です。

## 事前準備

使用する環境に合わせて [Windows（Git Bash）](docs/setup.md#windowsgit-bash)、[WSL（Ubuntu）](docs/setup.md#wslubuntu)、[Mac](docs/setup.md#mac) の手順を確認してください。GitHub でこのリポジトリへの書き込み権限が付いていることも確認します。準備で止まったら、当日その画面を見せて相談してください。

## 進め方

### 1. リポジトリを取得してブランチを作る

Windows は Git Bash、WSL は WSL のターミナル、Mac はターミナルで操作します。`<GitHub ID>` は自分の ID に置き換え、山括弧は入力しません。

```bash
git clone https://github.com/NUTFes/20261006-git-study.git
cd 20261006-git-study
git switch -c workshop/<GitHub ID>
```

**リポジトリ**はファイルと変更履歴のまとまり、**ブランチ**はほかの人の作業と分けるための作業場所です。`main` を直接編集せず、自分のブランチで進めます。

### 2. ページを編集して表示する

`index.html` をエディタで開き、次の3つの目印を自分の言葉に置き換えます。HTML のタグ（`<h1>` など）は残してください。

| 目印 | 入れる内容の例 |
| --- | --- |
| `CHANGE_ME_TITLE` | ブラウザのタブに出るページ名 |
| `CHANGE_ME_HEADING` | ページの見出し |
| `CHANGE_ME_MESSAGE` | 10文字以上のメッセージ |

保存したら、ファイルマネージャーから `index.html` をダブルクリックしてブラウザで開きます。3か所が表示され、目印が残っていないことを確認して、ページのスクリーンショットを撮ってください。余裕があれば Tailwind の `bg-slate-100` などの色も変えてみましょう（任意）。

### 3. 差分を見てコミットする

```bash
git status --short
git diff -- index.html
git add index.html
git commit -m "Update my workshop page"
```

**差分**は前の状態から変えた箇所、**コミット**は変更に名前を付けて履歴に残す操作です。`git status --short` で `index.html` だけが変更されていることを確認します。コミットのメッセージは、自分が何を変えたか分かる文章にして構いません。

### 4. push して PR を作る

```bash
git push -u origin workshop/<GitHub ID>
```

**push** は手元のコミットを GitHub に送る操作です。初回に認証画面が開いた場合は、GitHub アカウントでログインします。

GitHub のこのリポジトリを開き、表示される **Compare & pull request** から、取り込み先が `main` になっている PR を作ります。PR は「この変更を取り込んでください」という提案です。テンプレートの「変更したこと」を書き、「ブラウザで開いた」にチェックを入れ、スクリーンショットを本文の欄へドラッグ＆ドロップします。画像を PR 本文に添付する方法は [GitHub の説明](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files) も参照してください。

### 5. CI の結果を見る

PR の **Checks** にある `validate-submission` を確認します。**CI** は提出された変更を自動で確認する仕組みです。失敗した場合はエラー文を読み、HTML か PR 本文を直してください。HTML を直したらもう一度 `git add` → `git commit` → `git push` します。PR 本文だけを直した場合もチェックは自動で再実行されます。

よくある詰まりどころは [トラブルシューティング](docs/troubleshooting.md) にまとめています。

## 当日の時間配分

| 時間 | 内容 |
| --- | --- |
| 0–10分 | [Git と PR の流れ](docs/lecture.md) を説明 |
| 10–17分 | 環境確認、clone、ブランチ作成 |
| 17–30分 | HTML 編集、表示確認、スクリーンショット |
| 30–40分 | 差分確認、コミット、push |
| 40–55分 | PR 作成、CI の指摘を修正 |
| 55–60分 | 結果確認と振り返り |

コンフリクト解消や Docker は今回の必須課題には含めません。まずは「変更 → 確認 → 提案 → 自動チェック」の一連の流れを体験しましょう。
