"""
继承：
    单继承：子类可以访问父类所有的方法和属性
    多继承：当一个类有多个父类时，默认使用第一个父类的同名属性和方法
    多层继承：多个层级关系

    私有属性：在属性名和方法名前面加上两个下划线__

"""
class Master(object):
    def __init__(self):
        self.kongfu = '[煎饼果子的配方]'
        self.__money = 20000000

    def make_case(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(object):
    def __init__(self):
        self.kongfu = '[一中煎饼果子的配方]'

    def make_case(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独家煎饼果子的配方]'

    def make_case(self):
        super().make_case()
        print('--------------dh---------------')
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_case(self):
        Master.__init__(self)
        Master.make_case(self)

    def make_school_case(self):
        School.__init__(self)
        School.make_case(self)

class Tusun(Prentice):
    pass


obj = Prentice()
print(obj.kongfu)
obj.make_case()
print(Prentice.mro())
print('----------------------------------')


print(obj.make_master_case())
print(obj.make_school_case())
print(obj.make_case())