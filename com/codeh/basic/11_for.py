"""
for循环的使用：
    1.默认遍历的使用方式
    2.break与continue的语法使用
    python基础学习
"""
# 遍历字符串
str1 = 'hello'
for i in str1:
    print(i)

print('--------------------------------')

str2 = 'bigData'
for i in str2:
    print(i)
else:
    print('循环正常结束之后执行的代码....')

print('--------------------------------')

for i in str2:
    if i == 'D':
        print('遇到D不需要进行打印....')
        break
    print(i)
else:
    print('循环正常结束之后执行的代码....')

print('--------------------------------')

for i in str2:
    if i == 'D':
        print('遇到D不需要进行打印....')
        continue
    print(i)
else:
    print('循环正常结束之后执行的代码....')