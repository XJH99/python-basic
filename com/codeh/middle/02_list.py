"""
列表的常用操作：
    查找：
        1.index:返回指定数据的下标
        2.count:统计指定数据在列表中出现的次数
        3.len:返回列表的长度
        4.in:判断指定数据是否在列表中，存在返回True，不存在返回False
        5.not in：判断指定数据是否在列表中，不存在返回True，存在返回False
    增加：
        1.append：列表结尾追加数据
        2.extend：列表结尾追加数据，如果数据是⼀个序列，则将这个序列的数据逐⼀添加到列表
        3.insert：指定索引位置插入数据
    删除：
        1.del：删除列表，也可以删除列表指定位置数据
        2.pop：删除指定下标的数据（默认为最后一个），并返回该数据
        3.remove: 移除列表中某个数据的第一个匹配项
        4.clear：清空列表
    修改：
        1.修改指定下标元素
        2.reverse:逆序列表
        3.sort:排序
    复制：
        1.copy：复制一个新的列表

"""
name_list = ['tom', 'jack', 'jerry', 'marry', 'cat']
num_list = [9, 10, 3, 8, 11, 4, 7]
print(name_list[0])
print(name_list.index('marry'))
print(name_list.count('cat'))
print(len(name_list))
print('tom' in name_list)
print('tom' not in name_list)
print('--------------------------------------------')

name_list.append('say')
print(name_list)

name_list.extend(['rise', 'mom'])
print(name_list)

name_list.insert(1, 'codeh')
print(name_list)
print('--------------------------------------------')

del name_list[0]
print(name_list)

name_list.pop(1)
print(name_list)

name_list.remove('codeh')
print(name_list)
print('--------------------------------------------')

name_list[0] = 'carry'
print(name_list)

name_list.reverse()
print(name_list)

num_list.sort()
print(num_list)
print('--------------------------------------------')

name_list_bak = name_list.copy()
print(name_list_bak)
print('--------------------------------------------')

# 列表的遍历
for i in name_list_bak:
    print(i)
print('--------------------------------------------')

# 列表的嵌套，类似于二维数组
name_list_tmp = [['⼩明', '⼩红', '⼩绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]
print(name_list_tmp[1][0])
