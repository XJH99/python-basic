"""
while循环语句的使用:
    1.1~100之和
    2.1~100之间的偶数和
    3.打印矩形图案
    4.打印三角形图案
    5.九九乘法口诀

break与continue的区别使用：
    break是指结束当前循环，执行循环下面的代码
    continue指结束循环体中的此次循环，执行下一次循环

while .... else：
    当循环正常结束之后，要执行else后面的语句

"""

# 1 ~ 100之和
i = 1
res = 0
while i <= 100:
    res += i
    i += 1

print(f"1~100之和为{res}")
print('-------------------------------')

# 1 ~ 100之间的偶数和
num1 = 1
res1 = 0
while num1 <= 100:
    if num1 % 2 == 0:
        res1 += num1
    num1 += 1

print(f'1~100之间的偶数和为{res1}')
print('-------------------------------')

# break
num2 = 1
while num2 <= 5:
    if num2 == 4:
        print('吃饱了，不吃了')
        break
    print(f'吃了第{num2}个桃子')
    num2 += 1
print('-------------------------------')

# continue
num3 = 1
while num3 <= 5:
    if num3 == 4:
        print('这个桃子坏了，不吃了')
        num3 += 1
        continue
    print(f'吃了第{num3}个桃子')
    num3 += 1
print('-------------------------------')

# 打印矩形图案
k = 0
while k < 5:
    j = 0
    while j < 5:
        print('*', end=' ')
        j += 1
    print()
    k += 1
print('-------------------------------')

# 打印三角形图案
m = 0
while m < 5:
    n = 0
    while n <= m:
        print('*', end=' ')
        n += 1
    print()
    m += 1
print('-------------------------------')

# 打印九九乘法口诀
p = 1
while p <= 9:
    q = 1
    while q <= p:
        print(f'{q} * {p} = {q * p}', end='\t')
        q += 1
    print()
    p += 1
print('-------------------------------')

# while .... else ....
h = 1
while h <= 5:
    print(f'这次吃的是第{h}个桃子')
    h += 1
else:
    print("桃子全部吃完了.....")
