# 事前準備：Git と GitHub

この勉強会では Git のコマンドを使います。Node.js と Docker の準備は不要です。Windows は **Git Bash**、WSL は **WSL のターミナル**、Mac は **ターミナル**を使ってください。コマンド内の名前とメールアドレスは自分のものに置き換えます。

まずブラウザで GitHub にログインし、[教材リポジトリ](https://github.com/NUTFes/20261006-git-study)を開けるか確認してください。主催者が参加者に書き込み権限を付けます。

## Windows（Git Bash）

1. `git --version` が動けばインストール済みです。動かない場合は [Git for Windows](https://git-scm.com/download/win) をインストールし、**Git Bash** を開き直します。
2. Git Bash で次を実行します。

   ```bash
   git --version
   git config --global user.name "自分の名前"
   git config --global user.email "GitHubで使うメールアドレス"
   git config --global user.name
   git config --global user.email
   ```

3. Git for Windows に含まれる Git Credential Manager を使用している場合、最初の `git push` でブラウザの認証画面が開きます。認証に失敗したら [GitHub の HTTPS 認証ガイド](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github) を確認するか、当日相談してください。

## WSL（Ubuntu）

WSL がまだ使えない場合は、先に [Microsoft の WSL インストール手順](https://learn.microsoft.com/en-us/windows/wsl/install) に従ってください。インストールや再起動に時間がかかることがあるため、当日は Git Bash に切り替えても構いません。

WSL の Ubuntu ターミナルで次を実行します。Windows 側の Git Bash と WSL 側の Git は別の環境なので、設定も WSL 内で確認します。

```bash
git --version
# git が見つからない場合だけ実行
sudo apt update
sudo apt install git
git config --global user.name "自分の名前"
git config --global user.email "GitHubで使うメールアドレス"
git config --global user.name
git config --global user.email
```

作業ディレクトリは WSL 側のホームディレクトリ（`~`）を推奨します。HTTPS での `git push` 認証が未設定なら、[Microsoft の WSL 向け Git・Credential Manager 設定](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git) を参照してください。すでに SSH で GitHub へ push できる方は、普段の設定を使って構いません。

## Mac

ターミナルで `git --version` を実行します。Git がない場合は [Git の公式インストール案内](https://git-scm.com/download/mac) に従って導入し、ターミナルを開き直してください。

```bash
git --version
git config --global user.name "自分の名前"
git config --global user.email "GitHubで使うメールアドレス"
git config --global user.name
git config --global user.email
```

`git push` 時の認証は、設定済みの Git Credential Manager または SSH を利用します。未設定なら [GitHub の認証ガイド](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github) を確認してください。

## 3環境共通の確認

- `git --version` にバージョンが表示される。
- `git config --global user.name` と `git config --global user.email` に自分の設定が表示される。Git の名前は GitHub ID と同じでなくても構いません。
- GitHub にログインでき、教材リポジトリを開ける。

メールアドレスを公開したくない場合は、[GitHub のメール設定](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address) にある `noreply` アドレスを使えます。作業を始めるコマンドは [README](../README.md#進め方) にあります。
