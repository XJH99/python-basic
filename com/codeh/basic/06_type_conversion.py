"""
类型转换功能：当接收到的数据类型不符合我们的要求，我们需要对其进行转换处理
"""

num = input('请输入你的幸运数字：')
print(f'你的幸运数字为{num}')
print(type(num))

# 转换数据类型，将str类型转换为int类型
print(type(int(num)))

# 1.int类型转换为float类型
num1 = 10
print(float(num1))
print(type(float(num1)))

# 2.int类型转为str类型
num2 = 20
print(str(num2))
print(type(str(num2)))

# 3.将一个序列转为元组
list1 = [10, 20, 30]
print(tuple(list1))
print(type(tuple(list1)))

# 4.将一个元组转为一个列表
tuple1 = (10, 20, 30)
print(list(tuple1))
print(type(list(tuple1)))

# 5.eval() 将字符串中的数据转换为python表达式原本类型
str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(100, 200, 300)'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))
