# 追加課題

ハンズオンお疲れ様でした！
こちらは必須課題のPRを作り、CIが成功した人向けです。

開発中によくある場面ごとに、使えるGitコマンドを試してみましょう。
作業中の変更を調べたり、ステージに載せた前後で表示を比べたりします。

約10〜15分を目安に、できるところまで進めてください。
コマンドはWindowsのGit Bash、WSLのUbuntuターミナル、Macのターミナルで共通です。

まず教材リポジトリに移動します。フォルダ名が違う場合は、自分の環境に合わせてください。

```bash
cd 20261006-git-study
```

このページで作る`practice-note.txt`はコミットもpushもしません。
提出PRで変更できるファイルは`index.html`だけです。

## 1. 今いるブランチと作業の状態を調べる

最初に、今どのブランチで作業しているかを確認します。

```bash
git branch --show-current
```

自分の`feat/<GitHub ID>`が表示されましたか？
別の名前が出たら、この先へ進む前に主催者に声をかけてください。

次に、コミットしていない変更が残っているかを見ます。

```bash
git status
```

`git status`には、今いるブランチと、ステージに載せた変更・まだ載せていない変更が文章で表示されます。
ステージは、次のコミットに入れる変更を選んでおく場所です。
必須課題が終わった直後なら、変更がないことを示す`nothing to commit, working tree clean`が表示されます。

同じ情報を短く見たいときは、こちらを使います。

```bash
git status -sb
```

`-s`は短い表示、`-b`はブランチ情報を追加する指定です。
1行目の`## feat/<GitHub ID>`が手元のブランチ名です。
初回の`git push -u`が済んでいれば、`...origin/feat/<GitHub ID>`も続きます。
`origin/...`はGitHub上にある対応先のブランチです。
もし`[ahead 1]`と出たら、手元にまだpushしていないコミットが1つあります。

どの手元のブランチが、GitHub上のどのブランチと対応しているかも見られます。

```bash
git branch -vv
```

行頭に`*`が付いた行が、今いるブランチです。
その行の`[origin/feat/...]`が対応先で、必須課題の`git push -u origin ...`によって設定されました。
ここまでのコマンドは表示するだけなので、ファイルや履歴は変わりません。

## 2. PRに出した変更とコミットを読む

自分のPRで`index.html`をどう変えたか、ターミナルでも見てみましょう。

```bash
git diff main...HEAD -- index.html
```

`HEAD`は今いるブランチの最新コミットです。
`main...HEAD`は、手元の`main`と自分のブランチが分かれた時点からの変更を比べる指定です。
`--`の後ろにある`index.html`は、表示するファイルを絞っています。
`-`から始まる行が変更前、`+`から始まる行が変更後です。
GitHubのPRにある「Files changed」と見比べてみてください。

次は、コミットの履歴を短く表示します。

```bash
git log --oneline --decorate --graph --all -8
```

`--oneline`は1コミットを1行にまとめ、`-8`は最大8件に絞ります。
`--decorate`でブランチ名が付き、`--graph`で履歴の分かれ道が線になります。
`--all`は、手元で見られるほかのブランチの履歴も表示します。
少し複雑に見えても、まずは自分のコミットメッセージを探せればOKです。

自分のブランチにあり、手元の`main`にはないコミットだけを見たいなら、こちらです。

```bash
git log main..HEAD --oneline
```

今度は、最新の1コミットで変更したファイルと行数を見ます。

```bash
git show --stat HEAD
```

必須課題で3回コミットしたので、最新の1コミットとPR全体では表示内容が違うはずです。
自分のコミットがいくつあるか、PRで編集したファイルが表示されるか確かめてみてください。
この節のコマンドも、履歴を読むだけです。

## 3. ステージに載せる前後を比べる

ここから練習用の`practice-note.txt`を手元に作ります。
同じ名前のファイルがすでにある場合は、上書きせず主催者に相談してください。

```bash
printf 'Gitの練習メモ\n' > practice-note.txt
```

まず状態を見ます。

```bash
git status --short
```

`?? practice-note.txt`と出ます。
`??`は、Gitがまだ追跡していない新しいファイルという意味です。

次のコミットに入れる候補として、このファイルをステージに載せます。

```bash
git add practice-note.txt
```

もう一度、状態を見てみましょう。

```bash
git status --short
```

今度は`A  practice-note.txt`です。
左側の`A`は、ファイルの追加がステージに載っていることを表します。

ステージに載せていない変更を表示します。

```bash
git diff -- practice-note.txt
```

何も表示されませんが、変更が消えたわけではありません。
このコマンドは作業中のファイルとステージを比べるので、同じ内容なら空になります。

ステージに載っている内容は、こちらで確認できます。

```bash
git diff --staged -- practice-note.txt
```

`+Gitの練習メモ`が見えましたか？
ここまでで、`git add`の前後では見る場所が変わることが分かります。

では、ステージに載せた後でファイルにもう1行加えます。

```bash
printf '2行目を追加\n' >> practice-note.txt
```

```bash
git status --short
```

`AM practice-note.txt`と出ます。
左側の`A`は1行目がステージにあること、右側の`M`はその後でファイルを編集したことを表します。

2つの差分を順番に見てみましょう。

```bash
git diff -- practice-note.txt
```

こちらには、まだステージに載せていない2行目が出ます。

```bash
git diff --staged -- practice-note.txt
```

こちらには、すでにステージに載せた1行目が出ます。
今コミットした場合に記録されるのは1行目だけです。ここではコミットしません。

## 4. `restore`で元に戻す場所を選ぶ

まず、ステージに載せていない2行目だけを取り消します。
練習用の`practice-note.txt`を対象にしていることを確かめてから実行してください。

```bash
git restore -- practice-note.txt
```

ファイルの中身とGitの状態を、それぞれ確認します。

```bash
cat practice-note.txt
```

`Gitの練習メモ`だけが表示されます。2行目は消えました。

```bash
git status --short
```

表示は`A  practice-note.txt`に戻ります。
`git restore -- practice-note.txt`は、作業中のファイルをステージの内容に戻したからです。
取り消した2行目は消えるので、提出用の`index.html`には同じ操作を試さないでください。

続いて、ステージへの登録を取り消します。

```bash
git restore --staged practice-note.txt
```

```bash
git status --short
```

今度は`?? practice-note.txt`です。
`--staged`を付けると、ファイルをステージから外します。

```bash
cat practice-note.txt
```

1行目は残っています。
同じ`restore`でも、`--staged`の有無で戻す場所が違うと分かりましたか？

## 5. `stash`で作業中のファイルを一時退避する

別の作業をするために、今ある練習用ファイルを一時的に作業フォルダから片付けてみます。

```bash
git stash push -u -m "workshop practice" -- practice-note.txt
```

`stash`は作業中の変更を一時退避する機能です。
`practice-note.txt`はまだGitが追跡していないので、`-u`を付けて退避の対象に含めます。
`-m`で一覧に表示する名前を付け、`-- practice-note.txt`で対象をこのファイルだけに絞っています。

ファイルが片付いたか確認します。

```bash
git status --short
```

練習前にほかの変更がなければ、何も表示されません。
ファイルマネージャーでも、`practice-note.txt`が見えなくなっています。

一時退避の一覧を見ます。

```bash
git stash list
```

先頭に`workshop practice`があることを確認してください。
次の`pop`は一番新しい退避を戻すので、別のものが先頭にあれば主催者に相談してください。

```bash
git stash pop
```

戻ったか、状態と中身を見てみましょう。

```bash
git status --short
```

```bash
cat practice-note.txt
```

`?? practice-note.txt`と`Gitの練習メモ`が再び表示されます。
`git stash pop`は退避した変更を戻し、成功するとその退避を一覧から取り除きます。
エラーが出た場合は、ほかの変更を消さずに主催者へ画面を見せてください。

最後に、ファイルマネージャーで`practice-note.txt`だけを削除します。

```bash
git status --short
```

練習前に変更がなかった人は、何も表示されなければ終了です。お疲れ様でした！
必須課題の手順を見返したいときは[README](../README.md)に戻ってください。
