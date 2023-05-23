#事前にファイルをダウンロードする。
#ファイル名は以下。
#../data/h11_data04.html
#../data/h11_data05.html

#pandasで表を取得してデータを取り出す。
#取り出したデータをnumpyを使って計算していく
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#main関数
def main():
    #ファイルから表を取り込む。
    with open('../data/h11_data05.html') as f:
        prices_table=pd.read_html(f)            #物価
    with open('../data/h11_data04.html') as f:
        unemployment_rate_table=pd.read_html(f) #人口・雇用

    #必要な部分だけを取り出す。
    #消費者物価指数の前年比
    consumer_price_index_yoy=np.array([prices_table[0][0].to_numpy(),prices_table[0][4].to_numpy()]) 
    #ヘッダやテーブルの下部を取り除く。ヘッダは3行、下部は5行分不要。
    consumer_price_index_yoy=np.delete(consumer_price_index_yoy,list(range(3)),1)
    consumer_price_index_yoy=np.delete(consumer_price_index_yoy,list(range(-5,0)),1)
    consumer_price_index_yoy=consumer_price_index_yoy.astype(np.float32) #文字列から数値へ変換
    #完全失業率
    unemployment_rate=np.array([unemployment_rate_table[1][0].to_numpy(),unemployment_rate_table[1][5].to_numpy()])
    #先頭から3行目までと末尾の15行は不要
    unemployment_rate=np.delete(unemployment_rate,list(range(3)),1)
    unemployment_rate=np.delete(unemployment_rate,list(range(-15,0)),1)
    unemployment_rate=unemployment_rate.astype(np.float32) #文字列から数値へ変換
    #2023年現在、有効なデータの範囲は、1959年から2021年まで。
    #範囲外のデータを消す。
    #人口・雇用のデータは全体が使える。
    #物価のデータは先頭から4年分不要。
    consumer_price_index_yoy=np.delete(consumer_price_index_yoy,list(range(4)),1)
    #import pdb; pdb.set_trace()

    #データの数を合わせたので横軸を消費者物価指数（前年比）、縦軸を完全失業率としてグラフを描画する。
    #グラフの周辺の状態を設定。
    x_max=30 ; x_min=-30
    y_max=10 ; y_min=0
    plt.xlim(x_min,x_max)
    plt.ylim(y_min,y_max)
    plt.grid()
    plt.axhline(y=0,xmin=x_min,xmax=x_max,color="#000000",lw=3) #0の線を太めの黒い線で引く。
    plt.axvline(x=0,ymin=y_min,ymax=y_max,color="#000000",lw=3) #0の線を太めの黒い線で引く。
    plt.title("Phillips curve")
    plt.xlabel('Consumer Price Index (YoY)')
    plt.ylabel('Unemployment Rate')
    #データをプロットする。
    plt.plot(consumer_price_index_yoy[1],unemployment_rate[1],'.', markersize=10)
    plt.show() #グラフを描画する。

#main関数を実行する。
if __name__ == '__main__':
    main()