# -*- coding = utf-8 -*-
# @Time : 5:06 下午
# @Author : 阿童木
# @File : setup.py
# @software: PyCharm
import os

import pygame
from . import constants as C
from . import tools

pygame.init()
SCREEN=pygame.display.set_mode((C.SCREEN_W,C.SCREEN_H))#把屏幕做成一个常量
# TODO:path
GRAPHICS=tools.load_graphics(r'C:\Users\abc\Desktop\yesyesyes\马里奥游戏\resource\graphics')

# try:
#     abs = os.getcwd ()
#     GRAPHICS=pygame.image.load(abs)
# except FileNotFoundError:
#     try:
#         abs = os.getcwd()
#         sds=abs.split(r'\\')
#         sds.pop(-1)
#         ewr=r'\\'.join(sds)+r'\\resource\\graphics'
#         GRAPHICS = pygame.image.load(abs)
#     except Exception as e:
#         print(e)
