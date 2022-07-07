"""
字符串的常用方式：
    1.下标索引：下标索引访问从0开始进行访问
    2.切片：根据规则对操作的对象进行截取 序列[开始位置下标:结束位置下标:步⻓] 这个下标索引区间是左闭右开
    3.查找：find()，index()
    4.修改：replace(),spilt(),join(),capitalize(),title()
    5.判断：
"""
# 下标索引
name = 'jack'
print(name[1])
print('----------------------------------')

# 切片的操作
inter = 'www.baidu.com'
print(inter[2:5:1])
print(inter[2:5])
print(inter[:5])
print(inter[1:])
print(inter[:])
print(inter[::])
print(inter[:-1])
print(inter[-4:-1])
print(inter[::-1])

print('----------------------------------')

# find:检测某个⼦串是否包含在这个字符串中，如果在返回这个⼦串开始的位置下标，否则则返回-1
# 字符串序列.find(⼦串, 开始位置下标, 结束位置下标)
kms = 'how old are you'
print(kms.find('old'))
print(kms.find('old', 5, 10))
print('----------------------------------')

# index:检测某个⼦串是否包含在这个字符串中，如果在返回这个⼦串开始的位置下标，否则则报异常
print(kms.index('old'))
# print(kms.index('old', 5, 10))
print('----------------------------------')

# replace:字符串替换,
# 字符串序列.replace(旧⼦串, 新⼦串, 替换次数)
myStr = 'nice to meet to you'
print(myStr.replace('to', 'are'))
print(myStr.replace('to', 'are', 1))
print('----------------------------------')

# split:按照指定分隔符进行分割字符串，返回的类型是一个列表
# 字符串序列.split(分割字符, num)
print(myStr.split(' '))
print(myStr.split(' ', 1))
print('----------------------------------')

# join:将多个字符串合并成一个字符串
list1 = ['java', 'scala', 'flink', 'kafka']
print('_'.join(list1))
print('----------------------------------')

# capitalize:将字符串的第一个字符转为大写
print(myStr.capitalize())
print('----------------------------------')

# title:将字符串中每个单词首字母转大写
print(myStr.title())
print('----------------------------------')

# lstrip/rstrip/strip删除左右空格
str2 = ' come on baby '
print(str2.lstrip())
print(str2.rstrip())
print(str2.strip())
print('----------------------------------')

# startswith/endswith: 判断字符串前缀与后缀
print(myStr.startswith('nice'))
print(myStr.endswith('you'))
print('----------------------------------')

# isdigit: 如果是一个数字字符串返回True，不是就返回false，
print(myStr.isdigit())
print('----------------------------------')

# isalnum:如果字符串是字母数字字符串返回True，否则返回False
print(myStr.isalnum())
print('----------------------------------')

# isspace:如果字符换是空白字符串返回True，否则返回False
print(myStr.isspace())
print('----------------------------------')
