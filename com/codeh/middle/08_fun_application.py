"""
函数高级应用：

"""
# 学员列表信息
user_list = []


def info():
    print('-' * 20)
    print('欢迎登录学院管理系统')
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员信息')
    print('4.查询学员信息')
    print('5.显示所有学员信息')
    print('6.退出系统')
    print('-' * 20)


def add_user():
    """
    添加用户
    :return: user_list
    """
    user_id = int(input('请输入用户id：'))
    user_name = input('请输入用户姓名：')
    user_phone = input('请输入用户手机号：')

    for i in user_list:
        if user_name == i['user_name']:
            print('该用户已存在！')
            return

    # 定义一个字典封装用户信息
    user_dict = {'user_id': user_id, 'user_name': user_name, 'user_phone': user_phone}
    user_list.append(user_dict)
    print(user_list)


def del_user():
    """
    删除学员
    :return: NONE
    """

    del_id = int(input('请输入要删除的学员学号: '))

    for user in user_list:
        if del_id == user.get('user_id'):
            del_flag = input('确认要删除该学员吗？ yes or no : ')
            if del_flag == 'yes':
                index = user_list.index(user)
                print(f'删除用户的索引下标为{index}')
                del user_list[index]
            print(user_list)
            # 删除目标用户信息后退出循环
            break
    else:
        print('您输入的学员学号无效，请重新输入')


def update_user():
    """
    修改用户信息
    :return: NONE
    """
    while True:
        update_id = int(input('请输入要修改的学员学号： '))

        for user in user_list:
            if user['user_id'] == update_id:
                print(f'该学员的学号为{user["user_id"]}, 姓名为{user["user_name"]}, 手机号码为{user["user_phone"]}')
                # 获取列表的下标索引
                index = user_list.index(user)
                user_list[index]['user_id'] = int(input('请输入学号：'))
                user_list[index]['user_name'] = input('请输入姓名：')
                user_list[index]['user_phone'] = input('请输入手机号：')
                print(user_list)
                break
            else:
                print('输入的学员学号有误，请重新输入')


def search_info():
    """
    查询用户信息
    :return:
    """
    search_id = int(input('请输入要查询的用户id：'))

    for user in user_list:
        if user['user_id'] == search_id:
            print('查询到的用户信息如下：')
            print(f'查询到的该用户id为{user["user_id"]}, 姓名为{user["user_name"]}, 手机号码为{user["user_phone"]}')
            break
    else:
        print('查无此人')

def print_all():
    """
    打印所有学员信息
    :return:
    """
    print('已有的学员信息如下：')
    for user in user_list:
        print(f'用户id为{user["user_id"]}, 姓名为{user["user_name"]}, 手机号码为{user["user_phone"]}')


while True:

    # 1.打印系统信息
    info()

    # 2.选着功能信息
    user_num = input('请输入你选择的功能序号：')

    # 3.逻辑判断
    if user_num == '1':
        print('添加学员')
        add_user()
    elif user_num == '2':
        print('删除学员')
        del_user()
    elif user_num == '3':
        print('修改学员信息')
        update_user()
    elif user_num == '4':
        print('查询学员信息')
        search_info()
    elif user_num == '5':
        print('显示所有学员信息')
        print_all()
    elif user_num == '6':
        print('退出系统')
        break
    else:
        print('您输入的功能序号有误')
