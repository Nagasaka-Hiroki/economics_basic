#事前にファイルをダウンロードする。
#ファイル名は以下。
#../data/h11_data01.html
#../data/h11_data04.html

#pandasで表を取得してデータを取り出す。
#取り出したデータをnumpyを使って計算していく
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#main関数
def main():
    #ファイルから表を取り込む。
    with open('../data/h11_data01.html') as f:
        gdp_growth_rate_table=pd.read_html(f) #国民経済計算
    with open('../data/h11_data04.html') as f:
        unemployment_rate_table=pd.read_html(f) #人口・雇用

    #必要な部分だけを取り出す。
    #GCP成長率
    gdp_growth_rate=np.array([gdp_growth_rate_table[2][0].to_numpy(),gdp_growth_rate_table[2][3].to_numpy()]) 
    gdp_growth_rate=np.delete(gdp_growth_rate,list(range(5)),1)
    gdp_growth_rate=gdp_growth_rate.astype(np.float32) #文字列から数値へ変換
    #完全失業率
    unemployment_rate=np.array([unemployment_rate_table[1][0].to_numpy(),unemployment_rate_table[1][5].to_numpy()])
    #先頭から3行目までと末尾の15行は不要
    unemployment_rate=np.delete(unemployment_rate,list(range(3)),1)
    unemployment_rate=np.delete(unemployment_rate,list(range(-15,0)),1)
    unemployment_rate=unemployment_rate.astype(np.float32) #文字列から数値へ変換
    #完全失業率の前年との差を計算する。
    #変数名はdiff_unemployment_rateなどにするべきだが、実装の都合上そのままにする。
    unemployment_rate=np.append(unemployment_rate,[np.zeros(len(unemployment_rate[0]),np.float32)],axis=0)
    for i in range(len(unemployment_rate[0])):
        if i!=0:
            unemployment_rate[2][i]=unemployment_rate[1][i]-unemployment_rate[1][i-1]

    #2023年現在、有効なデータの範囲は、1960年から2021年まで。
    #範囲外のデータを消す。
    #GCP成長率 先頭(1956年)から4年分は不要
    gdp_growth_rate=np.delete(gdp_growth_rate,list(range(4)),1)
    #完全失業率の差分　先頭(1959年)から一年分は不要。
    unemployment_rate=np.delete(unemployment_rate,0,1)

    #データの数を合わせたので横軸をGDP成長率、縦軸を完全失業率の差分としてグラフを描画する。
    #グラフの周辺の状態を設定。
    x_max=15 ; x_min=-10
    y_max=1.5; y_min=-1.5
    plt.xlim(x_min,x_max)
    plt.ylim(y_min,y_max)
    plt.grid()
    plt.axhline(y=0,xmin=x_min,xmax=x_max,color="#000000",lw=3) #0の線を太めの黒い線で引く。
    plt.axvline(x=0,ymin=y_min,ymax=y_max,color="#000000",lw=3) #0の線を太めの黒い線で引く。
    plt.title("okun's law")
    plt.xlabel('GDP growth rate')
    plt.ylabel('Difference in unemployment rate from the previous year')
    #データをプロットする。
    plt.plot(gdp_growth_rate[1],unemployment_rate[2],'.', markersize=10,label="origin")
    #回帰直線を引く。
    a,b=np.polyfit(gdp_growth_rate[1],unemployment_rate[2],1)
    #回帰直線用に横軸の範囲を作る。
    dx=0.1
    x=np.arange(x_min,x_max+dx,dx)
    y=a*x+b
    plt.plot(x,y,label="fitting")
    plt.legend()
    plt.show() #グラフを描画する。
    corel=np.corrcoef(gdp_growth_rate[1],unemployment_rate[2])
    #相関係数行列は対称行列。xとyの相関を知りたければ、対角成分以外を取り出せば良い。
    print(corel[0][1])

#main関数を実行する。
if __name__ == '__main__':
    main()