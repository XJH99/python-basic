from com.codeh.manager.student import *


class StudentManager(object):
    def __init__(self):
        # 存储数据所用到的列表
        self.student_list = []

    def run(self):
        # 加载学员信息
        self.load_student()

        while True:
            self.show_menu(self)

            menu_num = int(input('请输入你需要的功能序号：'))

            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break

    @staticmethod
    def show_menu(self):
        print('请选择如下功能----------------')
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        print('7.退出系统')

    def add_student(self):
        name = input('请输入你的姓名：')
        gender = input('请输入你的性别：')
        tel = input('请输入你的电话号码：')

        student = Student(name, gender, tel)
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    def del_student(self):
        del_name = input('请输入要删除的学员姓名：')
        for student in self.student_list:
            if student.name == del_name:
                self.student_list.remove(student)
                break
        else:
            print('查无此人')

    def modify_student(self):
        modify_name = input('请输入要修改学员的姓名：')
        for student in self.student_list:
            if student.name == modify_name:
                student.name = input('请输入学员姓名：')
                student.gender = input('请输入学员性别：')
                student.tel = input('请输入学员电话号码：')

                print(f'修改学员信息成功，姓名{student.name}，性别{student.gender}，电话{student.tel}')
                break
        else:
            print('查无此人')

    def search_student(self):
        search_name = input('请输入要查询的用户姓名：')
        for student in self.student_list:
            if student.name == search_name:
                print(f'你要查询的学生姓名为{student.name}，性别为{student.gender}，电话为{student.tel}')
                break
        else:
            print('查无此人')

    def show_student(self):
        print('姓名\t性别\t手机号')
        for student in self.student_list:
            print(f'{student.name}\t{student.gender}\t{student.tel}')

    def save_student(self):
        f = open('student.data', 'w')
        # 将每一个实例对象转化为字典类型
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)

        f.write(str(new_list))

        f.close()

    def load_student(self):
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 读取数据
            data = f.read()

            # 将读取的字符串数据转化为对象后存储到学员列表之中
            new_list = eval(data)
            print(new_list)

            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]

        finally:
            f.close()
