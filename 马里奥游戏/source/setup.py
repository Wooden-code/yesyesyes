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

GRAPHICS=tools.load_graphics('resource/graphics')
#abs = os.getcwd ()
#GRAPHICS=tools.load_graphics(abs +'/resource/graphics')