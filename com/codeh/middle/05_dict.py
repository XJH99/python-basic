"""
字典的使用：类似于Java中的Map，一般为键值对类型
    新增：
        dict[key] = value （不存在则新增，存在的key就进行更新修改）
    删除：
        del:删除字典或删除字典中指定键值对
        clear:清空字典
    查找：
        dict[key]:按照key进行查找，存在返回对应的值，不存在报错
        get:按照key进行查找，查找不到就返回默认值
        keys：返回所有key的对象
        values：返回所有values的对象
        items：返回所有的键值对组合
    遍历：




"""

dict_code = {'name': 'rose', 'age': 10}
print(dict_code)

del dict_code['name']
print(dict_code)

dict_code.clear()
print(dict_code)

dict_people = {'name': 'rose', 'age': 10}
print(dict_people['name'])
print(dict_people.get('gender', '1'))

print(dict_people.keys())
print(dict_people.values())
print(dict_people.items())
print('-----------------------------------------')

# 打印所有的key
for key in dict_people.keys():
    print(key)
print('-----------------------------------------')

# 打印所有的value
for value in dict_people.values():
    print(value)
print('-----------------------------------------')

# 打印所有的键值对
for item in dict_people.items():
    print(item)
print('-----------------------------------------')

# 打印细分的键值对
for key, value in dict_people.items():
    print(f'{key} = {value}')
