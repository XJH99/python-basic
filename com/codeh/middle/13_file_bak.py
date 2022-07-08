"""
文件备份操作：用户输入当前目录下任意文件名，程序完成对该文件的备份功能
"""

# 接收用户输入的文件名
input_name = input('请输入你要备份的文件名：')

# 规划备份文件名
index = input_name.rfind('.')
print(index)

postfix = input_name[index:]
new_name = input_name[:index] + '[备份]' + postfix
print(new_name)

f_read = open(input_name, 'rb')
f_write = open(new_name, 'wb')

while True:
    content = f_read.read(1024)
    if len(content) == 0:
        break
    f_write.write(content)

f_read.close()
f_write.close()
