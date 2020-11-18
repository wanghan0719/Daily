"""
    界面逻辑
"""
import os

from bll import GameController


class GameConsoleView:

    def __init__(self):
        self.__controller = GameController()

    def main(self):
        self.__start()

        self.__update()

    def __start(self):
        # 产生两个新数字
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        # 绘制界面
        self.__draw_map()

    def __draw_map(self):
        # 清空终端
        os.system('clear')
        for line in self.__controller.map:
            for item in line:
                print(item, end=" ")
            print()

    def __update(self):
        while True:
            # 获取输入
            dir = input("请输入：")
            # 移动地图
            self.__move_map(dir)
            # 产生一个新数字
            self.__controller.generate_new_number()
            # 绘制界面
            self.__draw_map()
            # 游戏是否结束
            if self.__controller.is_game_over():
                print("游戏结束喽")

    def __move_map(self, dir):
        if dir == "w":
            self.__controller.move_up()
        elif dir == "s":
            self.__controller.move_down()
        elif dir == "a":
            self.__controller.move_left()
        elif dir == "d":
            self.__controller.move_right()
