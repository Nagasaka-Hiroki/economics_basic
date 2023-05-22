# 環境構築メモ
　Dockerを使って環境を構築する。そのため`Dockerfile`と`docker-compose.yml`ファイルを用意する。

以下のことを追加してファイルを作成する。

1. X11アプリが実行できるようにする。
1. 科学計算用のライブラリとグラフ描画用のライブラリを追加する。
1. HTML解析ができるライブラリを追加する。
1. 単体テストフレームワークをインストールする。

以上を踏まえて以下のコマンドで環境を構築する。

```bash
docker compose up -d --build
```

以上で基本的な構築は完了。追加でライブラリを入れる場合はDockerfileに追記する。

# 追記
## pytestに関して
　pytestをインストールしたが、コマンドが使えない。以下を参照。

- [Get Started — pytest documentation](https://docs.pytest.org/en/latest/getting-started.html#install-pytest)

上記の通り以下のコマンドに書き換える。

```bash
pip install -U pytest
```

また、念の為`pip install`にすべて`-U`オプションをつけておく。  
→うまく行かない。以下を参照。

- [pytestのインストール方法【Pythonライブラリ】｜資格マフィア](https://shikaku-mafia.com/pytest-install/)

管理者権限でインストールする。<b>
→うまく行った。これで更新する。