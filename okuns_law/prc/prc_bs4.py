#ドキュメントを参考に練習する。
from bs4 import BeautifulSoup
html_f=open('../data/h11_data01.html')
soup=BeautifulSoup(html_f,features="html.parser") #エラーにしたがってfeatures="html.parser"を追加する。
print(soup.title)
#div要素
tag=soup.div
print(tag['class'])
print(type(tag))
#table要素
tag=soup.td
print(tag['class'])
#idを指定して取得。
main_content=soup.find(id="contentsArea")
#print(main_content)

#bodyを指定する。
body=soup.body
table=body.find_all("table")
print(type(table))
print(table[0])

