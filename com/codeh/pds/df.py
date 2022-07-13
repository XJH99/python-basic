import pandas as pd

"""
DataFrame：是一个表格型的数据结构，含有一组有序列的列，每列可以是不同的值类型
        
    demo：pandas.DataFrame( data, index, columns, dtype, copy)
        data：一组数据
        index：索引值，或者可以称为行标签
        columns：列标签
        dtype：数据类型
        copy：拷贝数据，默认是false
    
"""
data = [['tom', 10], ['jack', 20], ['carry', 30]]
res1 = pd.DataFrame(data, columns=['name', 'age'], dtype=float)
print(res1)
print('-------------------------------------------------------')

# 没有对应的数据就为NaN
data1 = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5}]
df1 = pd.DataFrame(data1)
print(df1)
print('-------------------------------------------------------')

data2 = {
    'calories': [420, 380, 390],
    'duration': [50, 40, 45]
}

df2 = pd.DataFrame(data2)
# 返回第一行与第二行的数据
print(df2.loc[0])
print(df2.loc[1])
# 返回多行数据，使用，进行隔开
print(df2.loc[[0, 1]])
print('-------------------------------------------------------')

# 自定索引
df3 = pd.DataFrame(data2, index=['day1', 'day2', 'day3'])
print(df3)
print(df3.loc['day2'])


