"""
推导式：用一个表达式创建一个有规律的列表或控制一个有规律的列表，主要是简化代码
    列表推导式
    字典推导式：快速合并列表为字典或提取字典中目标数据
    集合推导式：

"""

list_case = []
for i in range(10):
    list_case.append(i)
print(list_case)

# 列表推导式生成
list_case_mode = [i for i in range(10)]
print(list_case_mode)

# 带过滤条件的列表推导式生成
list_case_mode1 = [i for i in range(10) if i % 2 == 0]
print(list_case_mode1)

# 多个for循环实现列表推导式
list_case_mode2 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list_case_mode2)
print('------------------------------------------------------------')

# 字典推导式
dict_case = {i: i * 2 for i in range(1, 5)}
print(dict_case)

# 两个列表合成为一个字典
list_col = ['name', 'age', 'gender']
list_val = ['jack', 20, 'male']
dict_case1 = {list_col[i]: list_val[i] for i in range(len(list_col))}
print(dict_case1)

# 提取列表中的目标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
dict_counts = {key: value for key, value in counts.items() if value > 200}
print(dict_counts)
print('------------------------------------------------------------')

list1 = [1, 1, 2]
set1 = {i ** 2 for i in list1}
print(set1)
