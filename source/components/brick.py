from .. import tools, setup
import pygame
from .. import constants as C
#from .powerup import create_powerup

class Brick(pygame.sprite.Sprite):
    def __init__(self,x,y,brick_type,group,color=None,name='brick'):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.brick_type=brick_type
        self.group=group
        self.name=name
 






        self.frame_index=0
        if self.brick_type==0:
            self.image= setup.GRAPHICS['bamboo.png']
        elif self.brick_type==1:
            self.image=setup.GRAPHICS['well.png']
        elif self.brick_type==2:
            self.image=setup.GRAPHICS['pipe.png']
        elif self.brick_type==3:
            self.image=setup.GRAPHICS['bamboo2.png']
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

        self.state='rest'
        self.gravity=C.GRAVITY

    def update(self):
        self.current_time = pygame.time.get_ticks()
        self.handle_states()

    def handle_states(self):
        if self.state == 'rest':
            self.rest()
        elif self.state == 'bumped':
            self.bumped()
        elif self.state == 'open':
            self.open()

    def rest(self):
        pass

    def go_bumped(self):
        self.y_vel = -7
        self.state = 'bumped'

    def bumped(self):
        self.rect.y += self.y_vel
        self.y_vel += self.gravity


        if self.rect.y > self.y + 10:  # 这里加一个10相当于多掉下10再回来，显得动画更流畅
            self.rect.y = self.y  # 不让宝箱掉下来
            self.state = 'rest'




    def open(self):

        pass

    def smashed(self,group):
       pass


class Debris(pygame.sprite.Sprite):
    def __init__(self,x,y,x_vel,y_vel):
        pygame.sprite.Sprite.__init__(self)
        self.image=tools.get_image(setup.GRAPHICS['tile_set.png'],68,20,8,8,(0,0,0),C.BRICK_MULTI)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.x_vel=x_vel
        self.y_vel=y_vel
        self.gravity=C.GRAVITY

    def update(self,*args):#后面这个是可变参数
        self.rect.x+=self.x_vel
        self.rect.y+=self.y_vel
        self.y_vel+=self.gravity
        if self.rect.y>C.SCREEN_H:
            self.kill()



