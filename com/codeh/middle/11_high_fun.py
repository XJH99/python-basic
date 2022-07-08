"""
内置高阶函数的使用：
    map：对每一个元素进行转换处理
    reduce：叠加运算场景
    filter：过滤操作
"""
import functools


def square(num):
    return num * 2


print(map(square, [1, 2, 3, 4, 5]))  # <map object at 0x0000028BED764548>
print(list(map(square, [1, 2, 3, 4, 5])))  # [2, 4, 6, 8, 10]
print('----------------------------------')


def func(a, b):
    return a + b


print(functools.reduce(func, [1, 2, 3, 4, 5]))


def filter_fun(num):
    return num % 2 == 0


print(filter(filter_fun, [1, 2, 3, 4, 5]))  # <filter object at 0x000002589A944AC8>
print(list(filter(filter_fun, [1, 2, 3, 4, 5])))
