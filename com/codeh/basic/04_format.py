"""
格式化输出：使用指定的格式化方式输出相应内容
"""

name = 'jack'
age = 20
weight = 75.5

print('我的名字叫%s' % name)
print('我今年%d岁了' % age)
print('我的体重是%.2f公斤' % weight)
# 下面两种的格式化输出比较常用
print('我的名字是%s，明年%d岁了' % (name, age))
print(f'我的名字是{name}, 明年{age}岁了')
