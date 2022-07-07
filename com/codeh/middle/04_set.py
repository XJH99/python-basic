"""
集合操作：
    增加数据：
        1.add：新增元素，在最前面追加元素
        2.update：追加的数据是序列
    删除数据：
        1.remove：删除集合中的指定数据，如果数据不存在则报错哦
        2.discard：删除集合中的指定数据，如果数据不存在也不会报错
        3.pop：随机删除集合中的某个数据，并返回这个数据
    查找数据：
        1.in：判断数据在集合序列中
        2.not in：判断数据不在集合序列中

"""

s1 = set()
s1.add(100)
s1.add(10)
s1.add(100)
print(s1)
print('------------------------------')

s1.update([200, 300])
s1.update('abc')
print(s1)
print('------------------------------')

s1.remove(100)
print(s1)

s1.discard(899)
print(s1)

str1 = s1.pop()
print(str1)
print('------------------------------')
