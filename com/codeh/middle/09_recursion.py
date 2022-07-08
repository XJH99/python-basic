"""
递归算法：函数内部自己调用自己，并且必须要有出口
"""


# 指定数字以内和
def recursion_sum(num):
    if num == 1:
        return 1

    return num + recursion_sum(num - 1)


result = recursion_sum(100)
print(result)
