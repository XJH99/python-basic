"""
lambda表达式的使用：lambda 参数列表: 表达式
    1.lambda表达式的参数可有可无，函数的参数在lambda表达式中完全适用
    2.lambda表达式能接收任何熟练的参数，但只能返回一个表达式的值

"""

fn1 = lambda: 100

print(fn1)  # <function <lambda> at 0x0000029074443D38>
print(fn1())  # 100

# 无参数
print((lambda: 100)())

# 一个参数
print((lambda a: a)('hello world'))

# 默认参数
print((lambda a, b, c=100: a + b + c)(10, 20))

# 可变参数
print((lambda *args: args)(10, 20, 30))
print((lambda **kwargs: kwargs)(name='python', age=20))

# 带判断
print((lambda a, b: a if a > b else b)(1000, 500))
