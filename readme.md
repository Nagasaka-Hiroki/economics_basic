# 明解 経済理論入門を読む
　明解 経済理論入門を読む。以下の本である。

- [明解　経済理論入門 - 株式会社あさ出版](http://www.asa21.com/book/b506709.html)

　ただ読むだけでもいいが、せっかくなのでPythonの練習を兼ねて計算コードを書く。基本的にはCUIで動くものとするが、グラフなどはウィンドウに出力して確認するように作成する。

作成は以下の環境で行った。実行環境はDockerで用意する。

|項目|バージョン|
|-|-|
|ホストOS|Ubuntu 22.04.2 LTS|
|Python|3.11.3|
|docker|24.0.1|
|docker compose|v2.18.1|
|ベースイメージ|[python:3.11.3-bullseye](https://hub.docker.com/layers/library/python/3.11.3-bullseye/images/sha256-181e49146bfdc8643ebe0f66cd06f27f42df40a0921438e96770dab09797effb)|

　実行環境の用意は以下のコマンドで行う。

```bash
docker compose up -d --build
```