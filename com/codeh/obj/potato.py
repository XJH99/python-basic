class Potato:

    def __init__(self):
        """
        cook_time：被烤时间
        cook_status：地瓜状态
        condiments：添加的调料
        """
        self.cook_time = 0
        self.cook_status = '生的'
        self.condiments = []

    def cook(self, time):
        """烤地瓜的方法"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_status = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_status = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_status = '熟了'
        elif self.cook_time >= 8:
            self.cook_status = '烤糊了'

    def add_condiments(self, condiment):
        """添加调料"""
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_status}, 添加的调料有{self.condiments}'


obj1 = Potato()
print(obj1)

obj1.cook(10)
print(obj1)

obj1.add_condiments('酱油')
print(obj1)

obj1.add_condiments('烧烤料')
print(obj1)
