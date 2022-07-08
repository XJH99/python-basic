"""
函数的使用
        作用：封装代码，高效的代码重用
        参数：分为实参与形参，实参是调用函数时传入的参数，形参是定义函数时的参数
        返回值：使用return关键字进行返回结果
        嵌套：函数里面可以调用其它的函数
        变量：
            1.局部变量：定义在函数内部，临时保存数据，即当函数调用完成之后，则销毁局部变量
            2.全局变量：定义在函数外部的公共区域，函数体内，外都能生效的变量(使用global关键字声明变量，可以在函数内部对全局变量进行修改)
        函数的参数：
            1.位置参数：调用函数时根据函数定义的参数位置来传递参数
            2.关键字参数：函数调用，通过"键=值"形式加以指定，可以让函数更加清晰容易使用
            3.缺省参数：就是默认参数，为参数提供默认值，调用函数时不传值就会使用默认值（所有位置参数必须出现在默认参数前，包括函数定义和调用）
            4.不定长参数：可变参数，用于不确定调用的时候会传递多少个参数（不传参）也可以的场景
        引用：在python中，值是靠引用来传递的
            1.可以使用id()方法判断两个变量是否为同一个值的引用
            2.int类型为不可变类型，列表为可变类型
        可变与不可变类型：数据能够直接进行修改，如果能直接修改那么就是可变，否则是不可变
            1.可变：列表，字典，集合
            2.不可变：int，float，str，tuple

"""


# 三数之和
def three_sum(num1, num2, num3):
    return num1 + num2 + num3


result = three_sum(10, 20, 30)
print(result)
print('-------------------------------------')

a = 10


def test_1():
    global a
    a = 200
    print(a)


test_1()

print('-------------------------------------')


# 函数参数case
def user_info(name, age, gender):
    print(f'你的名字是{name}，年龄为{age}，性别为{gender}')


user_info('tom', 20, '男')
user_info(name='jack', gender='女', age=20)


def user_info1(name, age, gender='男'):
    print(f'你的名字是{name}，年龄为{age}，性别为{gender}')


user_info1('carry', 10)
print('--------------------------------------')


# 包裹位置传递
def case1(*args):
    print(type(args))
    print(args)


case1('kill', 20)


# 包裹关键字传递
def case2(**kwargs):
    print(type(kwargs))
    print(kwargs)


case2(name='pet', age=99)
print('------------------------------------')

m = 1
n = m
print(id(m))
print(id(n))
m = 2
print(id(m))
print(id(n))

aa = [10, 20]
bb = aa
print(id(aa))
print(id(bb))
aa.append(30)
print(id(aa))
print(id(bb))
