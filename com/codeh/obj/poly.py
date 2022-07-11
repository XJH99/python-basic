"""
多态：父类的引用指向子类的具体实例对象
"""
class Dog(object):
    def work(self):
        print('指哪打哪')


class Dog1(Dog):
    def work(self):
        print('追击敌人')

class Dog2(Dog):
    def work(self):
        print('追查毒品')


class Person(object):
    def work_with_dog(self, dog):
        dog.work()

dog1 = Dog1()
dog2 = Dog2()

person = Person()
person.work_with_dog(dog1)
person.work_with_dog(dog2)