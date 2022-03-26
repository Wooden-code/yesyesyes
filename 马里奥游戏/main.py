# -*- coding = utf-8 -*-
# @Time : 4:15 下午
# @Author : 阿童木
# @File : main.py
# @software: PyCharm

# 程序主要入口
import pygame,os
from source import tools, setup,sound
from source.states import main_menu,load_screen,level,ask,body_title


def main():
    state_dict={#把所有阶段写成一个字典
        'main_menu':main_menu.MainMenu(),
        'load_screen':load_screen.LoadScreen(),
        'level':level.Level(),
        'ask':ask.Ask(),
        'body_title':body_title.Body_title()

    }

    game = tools.Game(state_dict,'main_menu')
    #state=main_menu.MainMenu()
    #state=load_screen.LoadScreen()
    #state=level.Level()

    game.run()


if __name__ == '__main__':
    pygame.mixer.music.load(os.path.abspath("resource/music/start.ogg"))  # 方法问题
    pygame.mixer.music.set_volume(1.0)  # 设置音量
    pygame.mixer.music.play(-1)
    main()
