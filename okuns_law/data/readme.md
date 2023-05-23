# オークンの法則のデータ
　プログラムを実行するたびにネットワークからデータを取得するのは良くないので、事前にデータをダウンロードする。このディレクトリはそのデータを保存する。

このディレクトリの中で以下のコマンドを実行する。（これは`../readme.md`にも記述しているが念の為）

```bash
curl https://www5.cao.go.jp/j-j/wp/wp-je22/h11_data01.html > ./h11_data01.html #国民経済計算
curl https://www5.cao.go.jp/j-j/wp/wp-je22/h11_data04.html > ./h11_data04.html #人口・雇用
```

上記コマンドを実行した上で、プログラムを実行する。