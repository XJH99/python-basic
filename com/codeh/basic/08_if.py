"""
条件语句：
    if
    if...else...
    if嵌套
"""

# 多重条件判断
age = int(input("请输入你的年龄："))

if age < 18:
    print(f'你的年龄为{age}，去和小孩一桌')
elif 18 <= age <= 60:
    print(f"你的年龄为{age}，去和大人一桌")
elif age > 60:
    print(f"你的年龄为{age}，去和老人一桌")
