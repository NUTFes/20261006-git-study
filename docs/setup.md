# 事前準備：Git と GitHub

この勉強会ではGitのコマンドを使います。Node.jsとDockerの準備は不要です。WindowsではGit Bash、WSLではUbuntuのターミナル、Macではターミナルを使ってください。コマンド内の名前とメールアドレスは自分のものに置き換えます。

まずブラウザでGitHubにログインし、[教材リポジトリ](https://github.com/NUTFes/20261006-git-study)を開けるか確認してください。主催者が参加者に書き込み権限を付けます。招待が届いた場合は、勉強会までに承諾してください。

## Windows（Git Bash）

`git --version`が動けばインストール済みです。動かない場合は[Git for Windows](https://git-scm.com/download/win)をインストールし、Git Bashを開き直します。Git Bashで次を実行してください。

```bash
git --version
git config --global user.name "自分の名前"
git config --global user.email "GitHubで使うメールアドレス"
git config --global user.name
git config --global user.email
```

Git for Windowsに含まれるGit Credential Managerを使用している場合、最初の`git push`でブラウザの認証画面が開きます。認証に失敗したら[GitHubのHTTPS認証ガイド](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)を確認するか、当日相談してください。

## WSL（Ubuntu）

WSLがまだ使えない場合は、先に[MicrosoftのWSLインストール手順](https://learn.microsoft.com/en-us/windows/wsl/install)に従ってください。インストールや再起動に時間がかかることがあるため、当日はGit Bashに切り替えても構いません。

WSLのUbuntuターミナルで次を実行します。Windows側のGit BashとWSL側のGitは別の環境なので、設定もWSL内で確認します。

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

作業ディレクトリにはWSL側のホームディレクトリ（`~`）をおすすめします。HTTPSでの`git push`認証が未設定なら、[MicrosoftのWSL向けGit・Credential Manager設定](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git)を参照してください。すでにSSHでGitHubへpushできる方は、普段の設定を使って構いません。

## Mac

ターミナルで`git --version`を実行します。Gitがない場合は[Gitの公式インストール案内](https://git-scm.com/download/mac)に従って導入し、ターミナルを開き直してください。

```bash
git --version
git config --global user.name "自分の名前"
git config --global user.email "GitHubで使うメールアドレス"
git config --global user.name
git config --global user.email
```

`git push`時の認証は、設定済みのGit Credential ManagerまたはSSHを利用します。未設定なら[GitHubの認証ガイド](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)を確認してください。

## 3環境共通の確認

- `git --version`にバージョンが表示される。
- `git config --global user.name`と`git config --global user.email`に自分の設定が表示される。Gitの名前はGitHub IDと同じでなくても構いません。
- GitHubにログインでき、教材リポジトリを開ける。招待が来ていれば承諾済み。

メールアドレスを公開したくない場合は、[GitHubのメール設定](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)にある`noreply`アドレスを使えます。作業を始めるコマンドは[README](../README.md#1-リポジトリを手元に用意する)にあります。
