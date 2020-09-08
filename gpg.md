## Prerequisites

```sh=
brew install gnupg
apt install gpg
```

## Generate key

> https://docs.github.com/ja/github/authenticating-to-github/generating-a-new-gpg-key

```sh=
gpg --full-gen-key
```

メールアドレスはGitHubに登録したものと同一のものにする

## Export public key

```sh=
gpg --list-secret-keys --keyid-format LONG
```


```sh=
~/.gnupg/pubring.kbx
-----------------------------
sec   rsa4096/3AA5C34371567BD2 2020-01-01 [SC]
      E4A8932BADC83860F7CA6926A9656A2875F36DBD
uid                 [  究極  ] NAME <E-MAIL>
ssb   rsa4096/42B317FD4BA89E7A 2020-01-01 [E]
```

3AA5C34371567BD2の部分をコピー
以下FINGER_PRINTと書く。

```sh=
gpg --armor --export FINGER_PRINT
```

# Add the GPG key to your GitHub account

> https://docs.github.com/ja/github/authenticating-to-github/adding-a-new-gpg-key-to-your-github-account

# Signing commits
署名するKeyを設定
```sh=
git config --global user.signingkey FINGER_PRINT
```

以下で毎回署名
```sh=
git commit -S
```

常に証明するなら以下で設定
```sh=
git config --global commit.gpgsign true
git config --global tag.gpgSign true # Tagへの署名もしたいなら
```