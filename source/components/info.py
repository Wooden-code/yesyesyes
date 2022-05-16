
#文字信息
import pygame
from .. import constants as C
from . import coin
from .. import setup,tools
pygame.font.init()

class Info:
    def __init__(self,state,game_info):#初始化 state阶段，以便管理各个阶段
        self.state=state
        self.state_labels = []
        self.game_info=game_info
        self.create_state_labels()
        self.create_info_labels()
        self.flash_coin=coin.FlashingCoin()
        self.count_word = setup.GRAPHICS['count_word.png']
        self.jinnang=setup.GRAPHICS['jinnang.png']
        self.blood=setup.GRAPHICS['blood.png']


    def create_state_labels(self):#创作某个阶段特有的文字，分数，金币，时间，等信息

        if self.state=='main_menu':#如果是主菜单阶段
          
            pass
        elif self.state=='load_screen':#加载页面
       
            pass

        elif self.state=='level':
          
            pass

    def create_info_labels(self):
      
        pass


    def create_label(self,label,size=54,width_scale=1.25,height_scale=1):#调整字
        #print(label)
        font=pygame.font.SysFont(None,size)
        label_image=font.render(label,None,(0,0,0),None)#把文字渲染成图片 白 理论上这里的1能够产生锯齿效果，但效果不明显，所以用以下方法
        rect=label_image.get_rect()#先把字体变小产生图片
        label_image=pygame.transform.scale(label_image,(int(rect.width*width_scale),int(rect.height*height_scale)))#放大产生锯齿效果


        return label_image

    def update(self):#不断更新时间，分数这样
       
        self.state_labels.append((self.create_label('x  {}'.format(self.game_info['num'])), (510, 60)))
        

    def draw(self,surface,level):#绘画
        ct=0
       
        surface.blit(self.state_labels[-1][0],self.state_labels[-1][1])#用blit方法画出来 对应 图片，位置
        surface.blit(self.count_word,(100,55))
        surface.blit(self.jinnang, (10, 20))
      
        while True:
            if ct<level.lives:
                surface.blit(self.blood, (30 + ct * 40, 130))
                # print("ii",ct)
                ct+=1
            else:
                break



