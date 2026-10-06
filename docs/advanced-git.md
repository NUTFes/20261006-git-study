# 追加課題

ハンズオンお疲れ様でした！
こちらは必須課題のPRを作りCIが成功した人向けです。

開発中に発生するそれぞれシーンごとにGitのコマンドと合わせてやればいいことをまとめています。
例えば、作業中の変更をどう読むか、ステージに載せると何が変わるかを手元の練習用ファイルで確かめます。

約10〜15分を目安に、できるところまで進めてください。
この資料にあるターミナルで実行するコマンドは、WindowsのGit Bash、WSLのUbuntuターミナル、Macのターミナル全てで同じように使えます。

最初に`cd 20261006-git-study`で教材リポジトリに移動し、自分の`workshop/<GitHub ID>`ブランチにいることを確かめます。
このページで作る`practice-note.txt`はコミットもpushもしません。提出PRで変更できるファイルは`index.html`だけです。

## 1. 今どのブランチで、何が残っているか

```bash
git status
git status -sb
git branch --show-current
git branch -vv
```

`git status`は、今いるブランチ、ステージに載せた変更、まだ載せていない変更を文章で表示します。`git status -sb`は短い表示にブランチ情報を加えます。`-s`が短い表示、`-b`がブランチ情報です。1行目は`## workshop/<GitHub ID>...origin/workshop/<GitHub ID>`のようになります。`origin/...`はGitHub上の対応するブランチです。手元でコミットした後、まだpushしていなければ`[ahead 1]`のような表示も加わります。

`git branch --show-current`は、今選んでいるローカルブランチの名前だけを表示します。`git branch -vv`は各ローカルブランチと、追跡しているリモートブランチを表示します。必須課題で最初に実行した`git push -u origin ...`の`-u`が、この対応を設定しました。ここまでのコマンドは状態を表示するだけで、ファイルも履歴も変更しません。

自分で確認：`git status -sb`の1行目に自分のブランチ名があり、提出後なら`origin/workshop/...`が続いていますか。

## 2. PRで提案した差分と履歴を読む

```bash
git diff main...HEAD -- index.html
git log --oneline --decorate --graph --all -8
git log main..HEAD --oneline
git show --stat HEAD
```

`HEAD`は、今選んでいるブランチの最新コミットを指します。`git diff main...HEAD -- index.html`は、手元の`main`と分かれた時点から、自分のブランチで`index.html`をどう変えたかを示します。`...`は共通の出発点を基準にする指定です。`--`の後ろはファイル名なので、このコマンドでは`index.html`だけを見ます。GitHubのPRにある「Files changed」と比べてみてください。

`git log --oneline --decorate --graph --all -8`は最大8件の履歴を短く表示します。`--decorate`はブランチ名、`--graph`は分岐の線、`--all`は手元で参照できるほかのブランチの履歴も加えます。`git log main..HEAD --oneline`は、自分のブランチにあり、手元の`main`にはないコミットを表示します。`git show --stat HEAD`は最新の1コミットで変わったファイルと行数を表示します。CIの修正で2回コミットした人は、`git show`とPR全体の差分が異なるはずです。

自分で確認：自分のコミットはいくつありますか。`git show --stat HEAD`に出たファイルは、PRで編集したファイルと一致しますか。これらのコマンドも履歴を変更しません。

## 3. ステージの前後で表示を比べる

ここから手元に`practice-note.txt`を作ります。すでに同名のファイルがある場合は、上書きせず主催者に相談してください。各コマンドの後で何が出るかを見てから次へ進みます。

```bash
printf 'Gitの練習メモ\n' > practice-note.txt
git status --short
git add practice-note.txt
git status --short
git diff -- practice-note.txt
git diff --staged -- practice-note.txt
```

作成直後は`?? practice-note.txt`です。`??`はGitがまだ追跡していない新しいファイルを表します。`git add`の後は`A  practice-note.txt`となります。左側の`A`は、このファイルの追加がステージに載った状態です。

通常の`git diff`は空になります。これは差分が消えたという意味ではありません。`git diff`は作業ファイルとステージの差分を見るため、両者が同じなら何も出ません。`git diff --staged`には、ステージに載せた`+Gitの練習メモ`が表示されます。

さらに、ステージに載せた後でファイルをもう1行編集します。

```bash
printf '2行目を追加\n' >> practice-note.txt
git status --short
git diff -- practice-note.txt
git diff --staged -- practice-note.txt
```

今度は`AM practice-note.txt`と表示されます。左側の`A`は1行目がステージにあること、右側の`M`はステージに載せた後で作業ファイルを変更したことを表します。通常の`git diff`には2行目、`git diff --staged`には1行目が出ます。このままコミットした場合、記録されるのはステージにある1行目だけです。ここではコミットしません。

## 4. `restore`の2種類を区別する

次の1行は、今追加した2行目だけを作業ファイルから取り消します。練習用ファイルであることを確認してから実行してください。

```bash
git restore -- practice-note.txt
cat practice-note.txt
git status --short
```

`cat`には1行目だけが表示され、`git status --short`は`A  practice-note.txt`になります。`git restore -- practice-note.txt`は、作業ファイルをステージに載っている内容へ戻しました。2行目は消えるので、自分の提出用`index.html`には同じ操作を試さないでください。

次はステージへの登録だけを取り消します。

```bash
git restore --staged practice-note.txt
cat practice-note.txt
git status --short
```

今度は`?? practice-note.txt`に戻ります。`git restore --staged`はステージから外す操作で、ファイルの1行目は残ります。同じ`restore`でも、`--staged`の有無で変わる場所が違います。`git status`とファイルの中身を両方見て確かめてください。

## 5. `stash`で作業中のファイルを一時退避する

`practice-note.txt`はGitがまだ追跡していないファイルです。次の`-u`を付けると、未追跡ファイルも一時退避に含まれます。

```bash
git stash push -u -m "workshop practice" -- practice-note.txt
git status --short
git stash list
```

`-- practice-note.txt`は退避する対象をこのファイルだけに限定します。`-m`は一覧で見分けるための名前です。退避後、`git status --short`が空になり、`git stash list`の先頭に`workshop practice`があれば成功です。ファイルマネージャーで見ると、この時点では練習用ファイルが作業フォルダから見えなくなっています。

戻す前に`git stash list`の先頭が自分の`workshop practice`か確認してください。ほかの人と共有しているリポジトリではありませんが、自分の別の一時退避があれば、`pop`は常に最新の項目を対象にします。

```bash
git stash pop
git status --short
cat practice-note.txt
```

`?? practice-note.txt`と1行目が再び表示されます。`git stash pop`は一時退避を作業フォルダへ戻し、成功するとその項目を一覧から取り除きます。エラーが出た場合は、ほかの変更を消さずに主催者へ画面を見せてください。

最後に、ファイルマネージャーで`practice-note.txt`だけを削除します。`git status --short`が空なら練習は終了です。自分が別に編集していたファイルまで削除しないでください。必須課題の手順は[README](../README.md)にあります。
