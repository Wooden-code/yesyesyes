# -*- coding = utf-8 -*-
# @Time : 5:04 下午
# @Author : 阿童木
# @File : main_menu.py.py
# @software: PyCharm
from moviepy.editor import *
import pygame,math,random
from .. import setup  # ..是上一级文件
from .. import tools
from .. import constants as C
from ..components import info  # 到上一级目录平行的components


class MainMenu:
    instance = None
    expanded_i = 1
    walk=60

    def __init__(self):
        game_info={
            'score':0,
            'coin':0,
            'num':0,
            'player_state':'small'#大的还是小的什么的

        }
        self.start(game_info)
    def start(self,game_info):
            self.game_info = game_info
            self.setup_background()
            self.paint1 = setup.GRAPHICS['paint_1.png']
            self.paint2 = setup.GRAPHICS['paint_2.png']
            self.paint3 = setup.GRAPHICS['paint_3.png']
            self.paint4 = setup.GRAPHICS['paint_4.png']
            self.paint5 = setup.GRAPHICS['paint_5.png']
            self.yyt=setup.GRAPHICS['yyt.png']
            self.lmt=setup.GRAPHICS['lmt.png']
            self.tyj=setup.GRAPHICS['tyj.png']
            self.lxr=setup.GRAPHICS['lxr.png']
            self.info = info.Info('main_menu', self.game_info)
            self.finished = False  # 只要这个阶段还在运行就不完结
            #self.next = 'introduction'  # 载入游戏阶段 也就是这里对应的下一阶段
            self.next='load_screen'
    def setup_background(self):  # 设置底图
            self.background = setup.GRAPHICS['main_title.png']
            self.background_rect = self.background.get_rect()
            self.background = pygame.transform.scale(self.background, (
                int(self.background_rect.width * C.BG_W_MULTI), int(self.background_rect.height * C.BG_H_MULTI)))
            self.viewport = setup.SCREEN.get_rect()  # 滑动窗口



    def setup_cursor(self):  # 设置光标
        self.cursor=pygame.sprite.Sprite()
        self.cursor.image= tools.get_image(setup.GRAPHICS['item_objects.png'], 24, 160, 8, 8, (0, 0, 0), C.PLAYER_MULTI)
        rect=self.cursor.image.get_rect()
        rect.x,rect.y=(220,360)
        self.cursor.rect=rect
        self.cursor.state='1P'#状态机



    def update_cursor(self,keys):
        if keys[pygame.K_UP]:
            self.cursor.state='1P'
            self.cursor.rect.y=360
        elif keys[pygame.K_DOWN]:
            self.cursor.state='2P'
            self.cursor.rect.y=405
        elif keys[pygame.K_RETURN]:#回车键按下进入游戏
            self.reset_game_info()#同时信息重置以下

            if self.cursor.state=='1P':
                self.finished=True
            elif self.cursor.state=='2P':
                self.finished=True
        self.welldone=tools.button(240, 250, 510, 520)
        self.check_if = tools.button(592, 653, 654, 759)


    def update(self, surface, keys):  # 更新操作
        self.update_cursor(keys)  # 上面的更新也会作为这里更新的一部分
        surface.blit(self.background,self.viewport)
        # surface.blit(self.background, self.viewport)  # 换上背景图和滑动窗口
        # surface.blit(self.cursor.image, self.cursor.rect)
        if self.check_if == 10 and MainMenu.expanded_i != 6:
            for i in range(MainMenu.expanded_i, 6):
                pygame.time.Clock().tick(5)
                surface.blit(eval(f"self.paint{i}"), (612 - i * 30, 650))
                pygame.display.flip()
                surface.blit(self.background, self.viewport)
                # pygame.time.Clock().tick(1)
            MainMenu.expanded_i = 6
        elif self.check_if == 8 and MainMenu.expanded_i == 6:
            clip = VideoFileClip(r'resource/video/111.mp4')
            # assert_approx_equal(float(clip.w) / float(clip.h), 16.0 / 9.0)
            # video_file = clip.crop(x1=clip.w / 8, x2=7 * clip.w / 8)
            # clip=clip.resize((1200,900))
            surface = pygame.display.set_mode(clip.size)
            # 全屏模式预览播放
            clip.preview()
            # 关闭并释放资源
            clip.close()

            self.finished = True
        elif MainMenu.expanded_i == 6:
            surface.blit(self.background, self.viewport)
            surface.blit(self.paint5, (462, 650))
        else:
            surface.blit(self.paint1, (582, 650))

        if self.welldone == 10 and MainMenu.expanded_i != 6:
            surface.blit(self.tyj,((math.sin(math.radians(MainMenu.walk))*400+487), abs(math.sin(math.radians(MainMenu.walk))*646)))
            surface.blit(self.lmt, (1000-(math.sin(math.radians(MainMenu.walk))*400+487), 700-abs(math.sin(math.radians(MainMenu.walk))*646)))
            surface.blit(self.lxr,(random.randint(0,1200),random.randint(0,800)))
            surface.blit(self.yyt, (random.randint(0,1200),random.randint(0,800)))
        MainMenu.walk+=1

    def reset_game_info(self):
        self.game_info.update({
            'score':0,
            'coin':0,
            'num':0,
            'player_state':0

        })


