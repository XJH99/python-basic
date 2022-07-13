import pandas as pd
"""
pandas读取csv文件数据：
"""

df = pd.read_csv('nba.csv')
# head读取前几行
print(df.head(10).to_string())
# tail读取后几行
print(df.tail(10).to_string())
print(df.info())

nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]

dict1 = {'name': nme, 'site': st, 'age': ag}
df1 = pd.DataFrame(dict1, index=[1, 2, 3, 4])
df1.to_csv('site.csv')