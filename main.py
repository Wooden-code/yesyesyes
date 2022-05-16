# -*- coding = utf-8 -*-
# @Time : 4:15 下午
# @Author : 阿童木
# @File : main.py
# @software: PyCharm

# 程序主要入口
import pygame,os,moviepy
from source import tools, setup,sound
from source.states import main_menu,load_screen,level,ask,body_title,part,drop,level2,level3,next_1,next_2


def main():
    state_dict={#把所有阶段写成一个字典
        'main_menu':main_menu.MainMenu(),
        'load_screen':load_screen.LoadScreen(),
        'level':level.Level(),
        'next_1':next_1.Next_1(),
        'ask':ask.Ask(),
        'body_title':body_title.Body_title(),
        'drop':drop.drop(),
        'next_2': next_2.Next_2(),
        'part':part.drop(),
        'level2': level2.Level2(),
        'level3':level3.Level3()

    }

    game = tools.Game(state_dict,'main_menu')
    #state=main_menu.MainMenu()
    #state=load_screen.LoadScreen()
    #state=level.Level()

    game.run()


if __name__ == '__main__':
    abs = os.getcwd()
    sds = abs.split(r'\\')
    # print(sds)
    # sds.pop(-1)
    ewr = r'\\'.join(sds) + r'\\resource\\music\\start.ogg'
    try:
        pygame.mixer.music.load(ewr)  # 方法问题
    except:
        ewr = sds[0].split('dist')[0] + r'\\resource\\music\\start.ogg'
        ewr = ewr.encode('utf-8')
        pygame.mixer.music.load(ewr)
    pygame.mixer.music.set_volume(1.0)  # 设置音量
    pygame.mixer.music.play(-1)
    main()
