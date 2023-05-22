import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('../data/h11_data01.html') as f:
    dfs=pd.read_html(f)

#print(len(dfs)) #5となるはず。
#print(type(dfs[2]))
#print(dfs[2]) #使うのは表3なのでそちらを確認する。
#print(dfs[2].head()) 
#print(dfs[2][3])
#print(dfs[2][0])

#表をnumpyに変換する。
x=np.array([dfs[2][0].to_numpy(),dfs[2][3].to_numpy()]) 
#print(x)

#不要な行を削除する。
rx=np.delete(x,list(range(5)),1)
#print(rx)

#文字になっているので数値に変換する。
rx=rx.astype(np.float32)
#print(rx)

#回帰分析
a,b=np.polyfit(rx[0],rx[1],1)

#a,b,c=np.polyfit(rx[0],rx[1],2) #二次関数でもできる。
#y=a*rx[0]**2+b*rx[0]+c

#グラフとして描画する。
plt.plot(rx[0],rx[1],'.', markersize=10,label="data1")
y=a*rx[0]+b
plt.plot(rx[0],y,label="data1(fitting)")
plt.xlim(1955,2025)
plt.ylim(-20,20)

#別のデータも比較する。
with open('../data/h11_data04.html') as f:
    dfs2=pd.read_html(f)

#２つ目の表の6列目が必要。
x2=np.array([dfs2[1][0].to_numpy(),dfs2[1][5].to_numpy()])

#不要な行を取り除く。
#先頭から3行目までは不要
x2=np.delete(x2,list(range(3)),1)
#末尾の15行は不要。
x2=np.delete(x2,list(range(-15,0)),1)
#文字列を数値に変換する。
x2=x2.astype(np.float32)
print(x2)

#合わせてプロットする。
plt.plot(x2[0],x2[1],'+',markersize=10,label="data2")

#同じく回帰分析
a,b=np.polyfit(x2[0],x2[1],1)
y=a*x2[0]+b
plt.plot(x2[0],y,label="data2(fitting)")

#凡例をつける。
plt.legend()

plt.show()