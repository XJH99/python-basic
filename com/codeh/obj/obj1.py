"""
魔方方法：
    初始化方法__init__：创建一个对象实例的时候就会自动的调用初始化方法
    __str__：重写对象的输出内容，类似于Java中的toString方法
    __del__：删除对象
"""

class Washer():

    """
    实例初始化方法
    self参数不需要开发者传递，python解释器会自动把当前对象引用传递过去
    """
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def print_info(self):
        # 类里面调用实例属性
        print(f'洗衣机的宽度是{self.width}, 高度是{self.height}')

    """
    类似于Java中的tostring方法，重写该方法自定义输出的对象内容
    """
    def __str__(self):
        return '这是海尔洗衣机的说明书'

    def __del__(self):
        print(f'{self}对象已被删除')

hair1 = Washer(100, 200)
hair1.print_info()
print(hair1)
del hair1