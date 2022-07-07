"""
运算符的使用：
    1.算术运算符
    2.赋值运算符
    3.复合赋值运算符
    4.比较运算符
    5.逻辑运算符
"""

# 多变量赋值运算符
num, str1, float1 = 1, 'hello', 3.14
print(num)
print(str1)
print(float1)

# 逻辑运算符
a = 1
b = 2
c = 3
print((a < b) and (b < c))  # True
print((a > b) and (b < c))  # False
print((a > b) or (b < c))  # True
print(not (a > b))  # True
