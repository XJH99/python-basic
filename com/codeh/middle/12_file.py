"""
文件操作：作用就是把一些数据存储存放起来，可以让程序下一次执行的时候直接使用，而不必重新制作一份
    1.获取文件对象
    2.文件读写操作
        read：读取全部的数据
        readline：读取一行数据
        seek：用来移动文件指针   ⽂件对象.seek(偏移量, 起始位置)
    3.关闭文件流


"""

# 获取文件对象
file = open('D:\\PY_IDEA\\python-basic\\data\\test.csv')
# file.write('hello world')
content = file.read()
print(type(content))
print(content)

# readline一次读取一行数据
c1 = file.readline()
print(c1)
c2 = file.readline()
print(c2)

c3 = file.seek(10, 0)
print(c3)

file.close()
