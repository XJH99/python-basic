"""
元组的常见操作：
    1.下标查找
    2.index：查找某个数据，如果数据存在返回对应的下标，否则报错
    3.count：统计某个数据在当前元组出现的次数
    4.len：统计元组中元素的个数

"""
tuple1 = ('hello', 10, True, 10.89)

print(tuple1[0])

print(tuple1.index(10))

print(tuple1.count(True))

print(len(tuple1))


