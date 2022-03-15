# -*- coding = utf-8 -*-
# @Time : 4:15 下午
# @Author : 阿童木
# @File : main.py
# @software: PyCharm

# 程序主要入口
import pygame
from source import tools, setup
from source.states import main_menu,load_screen,level


def main():
    state_dict={#把所有阶段写成一个字典
        'main_menu':main_menu.MainMenu(),
        'load_screen':load_screen.LoadScreen(),
        'level':level.Level(),
        'game_over':load_screen.GameOver()
    }

    game = tools.Game(state_dict,'main_menu')
    #state=main_menu.MainMenu()
    #state=load_screen.LoadScreen()
    #state=level.Level()

    game.run()


if __name__ == '__main__':
    main()
