# 困ったとき

| 状況 | 確認すること |
| --- | --- |
| `git: command not found` | [準備ガイド](setup.md)で自分の環境のGitインストールを確認し、ターミナルを開き直す。 |
| `Author identity unknown` | `git config --global user.name`と`git config --global user.email`を設定する。WSLではWSL内で設定する。 |
| `fatal: not a git repository` | `cd 20261006-git-study`で取得したフォルダに移動する。 |
| `git switch`が使えない | Gitのバージョンを確認する。更新が難しければ主催者に相談する。 |
| `git push`で認証・権限エラーになる | GitHubにログインし、招待を承諾しているか確認する。書き込み権限があるかは主催者に確認する。認証方法は[準備ガイド](setup.md)を参照する。 |
| ページが変わらない | 編集した`index.html`を保存し、ブラウザで開いているファイルの場所を確認して再読み込みする。 |
| ページにTailwindの色や余白が付かない | [Tailwind Play CDN](https://tailwindcss.com/docs/installation/play-cdn)を読み込むため、インターネット接続を確認する。文章とロゴはネットワークがなくても表示できる。 |
| CIに`CHANGE_ME_`と出る | `index.html`の3つの目印をすべて置き換える。 |
| CIにスクリーンショットがないと出る | PR本文の「スクリーンショット」欄に画像をドラッグ＆ドロップする。アップロード後に`![...](https://...)`の形の行が入ったら保存する。画像ファイルはコミットしない。 |
| PR本文を直してもCIが赤いまま | 新しい`validate-submission`の実行が始まっているか確認する。少し待っても始まらなければページを更新する。 |

エラーメッセージをそのまま主催者に見せてもらえると、原因を特定しやすくなります。
