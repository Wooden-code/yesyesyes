
import pygame,sys,os

class Music_BG:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.game_info=None
    #背景音乐
    def update(self,surface,keys):#jinrule
        # TODO:path
        abs = os.getcwd()
        sds = abs.split(r'\\')
        # print(sds)
        # sds.pop(-1)
        ewr = r'\\'.join(sds) + r'\\resource\\music\\start.ogg'
        try:
            pygame.mixer.music.load(ewr)  # 方法问题
        except:

            pygame.mixer.music.load(r'C:\Users\abc\Desktop\yesyesyes\马里奥游戏\resource\music\main.ogg')
        pygame.mixer.music.set_volume(1.0)  # 设置音量
        pygame.mixer.music.play(-1)#循环播放


    #特定音效

