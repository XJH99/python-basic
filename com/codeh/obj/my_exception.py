# 自定义异常，要继承Exception类

class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        # 设置抛出异常的描述信息
        return f'你输入的长度是{self.length}, 不能少于{self.min_len}个字符'


def main():
    try:
        con = input('请输入密码：')
        if len(con) < 3:
            raise ShortInputError(len(con), 3)
    except Exception as result:
        print(result)
    else:
        print('密码已输入完成')


main()
