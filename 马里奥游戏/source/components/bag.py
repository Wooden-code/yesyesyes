import pygame
from .. import constants as C
from . import coin,player
from .. import setup,tools
from ..states import level
pygame.font.init()

class Bag:
    def __init__(self,state,game_info):#初始化 state阶段，以便管理各个阶段
        self.state=state
        self.state_labels = []
        self.game_info=game_info
        self.create_state_labels()
        self.flash_coin=coin.FlashingCoin()
        self.bag_image=[setup.GRAPHICS['you_1.png'],setup.GRAPHICS['you_2.png']]
        self.bag=[setup.GRAPHICS['han_1.png'],      setup.GRAPHICS['ji_1.png'],      setup.GRAPHICS['you_1.png'],      setup.GRAPHICS['pronounce_13.png'],setup.GRAPHICS['you_4.png'],
                  setup.GRAPHICS['sentence1.png'],  setup.GRAPHICS['sentence_11.png'],setup.GRAPHICS['sentence_12.png'], setup.GRAPHICS['you_2.png'],       setup.GRAPHICS['you_3.png'],       setup.GRAPHICS['pronounce_1.png'],
                  setup.GRAPHICS['pronounce_2.png'],setup.GRAPHICS['han_2.png'],     setup.GRAPHICS['pronounce_4.png'],setup.GRAPHICS['ji_3.png'],        setup.GRAPHICS['pronounce_11.png'],setup.GRAPHICS['pronounce_9.png'],
                  setup.GRAPHICS['sentence2.png'],  setup.GRAPHICS['han_3.png'],     setup.GRAPHICS['pronounce_3.png'],setup.GRAPHICS['sentence_13.png'],  setup.GRAPHICS['pronounce_12.png'],setup.GRAPHICS['pronounce_10.png'],
                  setup.GRAPHICS['sentence7.png'],  setup.GRAPHICS['han_4.png'],     setup.GRAPHICS['ji_2.png'],       setup.GRAPHICS['sentence5.png'],   setup.GRAPHICS['ji_4.png'],        setup.GRAPHICS['pronounce_7.png'],
                  setup.GRAPHICS['sentence_8.png'],  setup.GRAPHICS['sentence3.png'], setup.GRAPHICS['sentence4.png'],  setup.GRAPHICS['sentence6.png'],   setup.GRAPHICS['pronounce_6.png'], setup.GRAPHICS['pronounce_8.png'],
                  setup.GRAPHICS['sentence_9.png'],  setup.GRAPHICS['sentence_10.png'],setup.GRAPHICS['pronounce_5.png'],setup.GRAPHICS['sentence_15.png'],  setup.GRAPHICS['sentence_16.png']]


    def create_state_labels(self):#创作某个阶段特有的文字，分数，金币，时间，等信息

        if self.state=='main_menu':#如果是主菜单阶段

            pass
        elif self.state=='load_screen':#加载页面

            pass

        elif self.state=='level':
            pass

    def add_bag_labels(self):

        pass


    def create_label(self,label,size=54,width_scale=1.25,height_scale=1):#调整字

        pass

    def update(self,level):#不断更新时间，分数这样


        #self.bag.append(level.words_all_group)
        pass

    def draw(self,surface):#绘画


        surface.blit(self.bag_image[0],(0,0))#用blit方法画出来 对应 图片，位置

        #surface.blit(self.count_word,(10,55))

