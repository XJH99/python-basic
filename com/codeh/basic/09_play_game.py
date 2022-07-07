import random

"""
需求分析：猜拳游戏，玩家与电脑进行猜拳，玩家手动出拳，电脑随机出拳；
输赢判断：
    玩家赢：玩家石头 -》 电脑剪刀，玩家剪刀 -》 电脑布，玩家布 -》 电脑石头
    平局：玩家石头 -》 电脑石头，玩家石头 -》 电脑石头，玩家布 -》 电脑布
    玩家输：上面情况都不满足，那玩家就输了
0 -》 石头， 1 -》 剪刀，2 -》 布
"""

player = int(input("请输入你的猜拳：0 -》 石头， 1 -》 剪刀，2 -》 布 "))
computer = random.randint(0, 2)
print(computer)

if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')
