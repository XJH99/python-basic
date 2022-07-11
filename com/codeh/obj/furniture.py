class Furniture():
    def __init__(self, name, area):
        """
        初始化方法
        :param name:家具名称
        :param area: 家具占地面积
        """
        self.name = name
        self.area = area

class Home():
    def __init__(self, address, area):
        """
        初始化方法
        :param address:地理位置
        :param area:房间面积
        """
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []

    def __str__(self):
        return f'房子坐落于{self.address}, 占地面积{self.area}，剩余面积{self.free_area}，家具有{self.furniture}'

    def add_furniture(self, item):
        """
        添加家具
        :param item: 添加的家具实例
        :return:
        """
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('家具太大，剩余面积容纳不下')

bed = Furniture('双人床', 6)
sofa = Furniture('沙发', 10)
home = Home('北京', 100)
print(home)

home.add_furniture(bed)
print(home)

home.add_furniture(sofa)
print(home)

