"""
异常
    语法：
        try:
         可能发⽣错误的代码
        except 异常类型:
         如果捕获到该异常类型执⾏的代码
"""

try:
    print(1 / 0)
except (NameError, ZeroDivisionError) as error_info:
    # 打印异常信息
    print(error_info)
    print('算数异常')

try:
    f = open('test.txt', 'r')
except Exception as info:
    print(info)
    f = open('test.txt', 'r')
else:
    print('不存在异常')
finally:
    f.close()
