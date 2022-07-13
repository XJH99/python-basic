import pandas as pd

"""
    Series：类似于表格中的一个列，就像一维数组，可以保存任何数据类型
    demo：
        pandas.Series( data, index, dtype, name, copy)
        data：数据
        index：数据索引标签
        dtype：数据类型，默认会自己判断
        name：设置名称
        copy：拷贝数据，默认为false
"""
a = [1, 2, 3]
var = pd.Series(a)
print(var[1])

# 指定索引值
data1 = ['common', 'case', 'tmp']
res = pd.Series(data1, index=['x', 'y', 'z'])
print(res)

# 使用k/v对象创建series，key就变成了索引值
sites = {1:'google', 2:'common', 3:'case'}
res1 = pd.Series(sites)
print(res1)

# 指定名称以及指定数据的索引
res2 = pd.Series(sites, index=[1,2], name='case-by-case')
print(res2)
