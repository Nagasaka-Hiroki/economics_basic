# フィリップス曲線のデータ
　プログラムを実行するために必要なデータをダウンロードする。事前にコマンドでダウンロードする。以下を実行する。

```bash
curl https://www5.cao.go.jp/j-j/wp/wp-je22/h11_data04.html > ./h11_data04.html #人口・雇用
curl https://www5.cao.go.jp/j-j/wp/wp-je22/h11_data05.html > ./h11_data05.html #物価
```

データはダウンロードして所得可能なので、`.gitignore`で除外する。