import pandas as pd

"""
使用pandas进行数据清洗操作:
    1.pandas会把n/a和NA当作空数据，不过我们也可以自定义指定空数据类型
"""

"""
miss_value = ['n/a', 'na', '--']
data = pd.read_csv('property-data.csv', na_values=miss_value)
print(data['NUM_BEDROOMS'])
print(data['NUM_BEDROOMS'].isnull())
print(data.to_string())
"""

"""
参数说明：
    axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列
    how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行
    thresh：设置需要多少非空值的数据才可以保留下来的
    subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数
    inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据
"""

"""
data = pd.read_csv('property-data.csv')
print(data.to_string())
# data.dropna(inplace=True)
# data.dropna(subset=['ST_NUM'], inplace=True)
# data.fillna(12345, inplace=True)
# data['ST_NUM'].fillna(1234, inplace=True)

avg = data['ST_NUM'].mean()
data['ST_NUM'].fillna(avg, inplace=True)
print(data.to_string())
"""

"""
data = {
    "Date": ['2020/12/01', '2020/12/02', '20201226'],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string)
"""

person = {
    "name": ['Google', 'Runoob', 'Taobao'],
    "age": [50, 200, 12345]
}

data = pd.DataFrame(person)

for i in data.index:
    if data.loc[i, 'age'] > 120:
        # data.loc[i, 'age'] = 120
        data.drop(i, inplace=True)

print(data.to_string)
