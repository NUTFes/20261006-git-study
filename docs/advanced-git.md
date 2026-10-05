# 追加課題：Gitの状態を読み、変更を一時退避する

必須課題のPRを作り、CIが成功した人向けです。ここでは手元の状態を調べ、練習用ファイルでステージと一時退避を試します。約10〜15分で、できるところまで進めてください。WindowsのGit Bash、WSLのUbuntuターミナル、Macのターミナルで同じコマンドを使えます。

最初に`cd 20261006-git-study`でリポジトリに移動してください。以下のコマンドは、自分の`workshop/<GitHub ID>`ブランチで実行します。練習用の`practice-note.txt`はコミットもpushもしません。提出PRでは`index.html`だけを変更するためです。

## 1. 今いるブランチと作業状態を確認する

```bash
git status -sb
git branch --show-current
git branch -vv
```

`git status -sb`の1行目には`## workshop/<GitHub ID>`が表示されます。初回のpushが済んでいれば、`...origin/workshop/<GitHub ID>`も表示されます。`-s`は短い表示、`-b`はブランチ情報の追加です。`git branch --show-current`は現在のブランチ名だけを表示します。`git branch -vv`では、各ローカルブランチと、追跡しているリモートブランチを確認できます。どのコマンドも状態を表示するだけです。

考えてみよう：自分のブランチは、今GitHub上のどのブランチと対応していますか。

## 2. 差分とコミットを読む

```bash
git diff main...HEAD -- index.html
git log --oneline --decorate --graph --all -8
git log main..HEAD --oneline
git show --stat HEAD
```

`git diff main...HEAD -- index.html`は、`main`と分かれた時点から自分のブランチまでに`index.html`がどう変わったかを表示します。`...`は、共通の出発点から現在のブランチまでの差分を見る指定です。`--`より後ろはファイル名です。

`git log --oneline --decorate --graph --all -8`は、最大8件のコミットを短く表示します。`--decorate`はブランチ名を付け、`--graph`は履歴の分かれ方を線で示し、`--all`は手元で参照できるブランチの履歴も含めます。`git log main..HEAD --oneline`は、自分のブランチにあり、手元の`main`にはないコミットを表示します。`git show --stat HEAD`は直近のコミットで変わったファイルを表示します。どれも履歴を変更しません。

考えてみよう：PRの「Files changed」に見える変更と、最初の`git diff`の結果は対応していますか。

## 3. ステージに載せる前後を比べる

これから`practice-note.txt`を手元に作ります。すでに同名のファイルがある場合は、上書きせず主催者に相談してください。

```bash
printf 'Gitの練習メモ\n' > practice-note.txt
git status --short
git add practice-note.txt
git status --short
git diff -- practice-note.txt
git diff --staged -- practice-note.txt
```

作成直後は`?? practice-note.txt`です。`??`はGitがまだ追跡していないファイルを表します。`git add`の後は`A  practice-note.txt`になります。左側の`A`はステージに追加された状態です。そのため、ステージ前の差分を表示する`git diff`には何も出ません。`git diff --staged`には、追加する行が`+Gitの練習メモ`と表示されます。

次に、コミットへ含めないようステージから外します。

```bash
git restore --staged practice-note.txt
git status --short
```

表示は再び`?? practice-note.txt`です。`git restore --staged`はステージへの登録を取り消します。練習用ファイルそのものは残ります。`git add`した内容を確かめてからコミットする習慣を付けましょう。

## 4. 作業中のファイルを一時退避する

```bash
git stash push -u -m "workshop practice" -- practice-note.txt
git status --short
git stash list
git stash pop
git status --short
```

`git stash push`は作業中の変更を一時的に保存します。`-u`を付けると、まだGitが追跡していない`practice-note.txt`も対象になります。`-m`は一覧に表示する名前です。`-- practice-note.txt`で、このファイルだけを対象にします。退避した直後の`git status --short`は空になり、`git stash list`には`workshop practice`が表示されます。

`git stash pop`で最新の退避内容を手元に戻します。再び`?? practice-note.txt`と表示されれば成功です。`pop`は適用に成功すると、その退避項目を一覧から取り除きます。ほかの作業の退避がすでにある場合は、`git stash list`の先頭が`workshop practice`か確認してから`pop`してください。

練習が終わったら、ファイルマネージャーで`practice-note.txt`だけを削除します。最後に`git status --short`で何も表示されないことを確認してください。自分の別の変更がある場合は、その変更まで消さないでください。

必須課題に戻るときは[README](../README.md#今日の進め方)を開いてください。
