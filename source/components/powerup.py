
import pygame,os
from .. import setup,tools
from ..components import enemy,player
from .. import constants as C

def create_powerup(centerx,centery,type):#根据主角不同状态出不同的东西
    return Mushroom(centerx,centery)

def gogo(num):
    if num==1:
        fii='test1.ogg'
    abs = os.getcwd()
    sds = abs.split(r'\\')
    ewr = sds[0] + r'\\resource\\music\\'+fii
    try:
        pygame.mixer.Sound(ewr).play()
    except:
        ewr = sds[0].split('dist')[0] + r'resource\\music\\' + fii
        pygame.mixer.Sound(ewr).play()
    return 0



class Powerup(pygame.sprite.Sprite):
    def __init__(self,centerx,centery,frame_rects,name):
        pygame.sprite.Sprite.__init__(self)

        self.frames=[]
        self.frame_index=0
        if name=='fireball':
            self.frames=[setup.GRAPHICS['yy_1.png'],setup.GRAPHICS['yy_2.png'],setup.GRAPHICS['yy_3.png'],setup.GRAPHICS['yy_4.png']]
        elif name=='slj':
            self.frames = [setup.GRAPHICS['slj1.png'], setup.GRAPHICS['slj2.png']]
        self.image=self.frames[self.frame_index]
        self.rect=self.image.get_rect()
        self.rect.centerx=centerx
        self.rect.centery=centery
        self.origin_y=centery-self.rect.height/2+10

        self.x_vel=0
        self.direction=1#向右
        self.y_vel=-1#向上长出来
        self.gravity=1
        self.max_y_vel=8

    def update_position(self, level):
        self.rect.x += self.x_vel
        self.check_x_collisions(level)
        self.rect.y += self.y_vel
        self.check_y_collision(level)

        if self.rect.x<0 or self.rect.y>C.SCREEN_H:
            self.kill()


    def check_x_collisions(self, level):
        sprite = pygame.sprite.spritecollideany(self, level.ground_items_group)
        if sprite:
            self.direction = 1 if self.direction == 0 else 0
            if self.direction:  # 向右#这里主要是龟壳碰撞希望回来
                self.direction = 0
                self.rect.right = sprite.rect.left
            else:
                self.direction = 1
                self.rect.left = sprite.rect.right
            self.x_vel *= -1



    def check_y_collision(self, level):
        check_group = pygame.sprite.Group(level.ground_items_group, level.box_group, level.brick_group)
        sprite = pygame.sprite.spritecollideany(self, check_group)
        if sprite:
            if self.rect.top < sprite.rect.top:
                self.rect.bottom = sprite.rect.top
                self.y_vel = 0
                self.state = 'walk'
        level.check_will_fall(self)

class Mushroom(Powerup):
    def __init__(self,centerx,centery):
        self.name = 'mushroom'
        Powerup.__init__(self,centerx,centery,[(0,0,16,16)],self.name)
        self.x_vel=2
        self.state='grow'
        self.name='mushroom'

    def update(self,level):

        if self.state=='grow':
            self.rect.y+=self.y_vel
            if self.rect.bottom<self.origin_y:
                self.state='walk'
        elif self.state=='walk':
            pass
        elif self.state=='fall':
            if self.y_vel<self.max_y_vel:
                self.y_vel+=self.gravity
        if self.state!='grow':
           self.update_position(level)

class Fireball(Powerup):
    def __init__(self,centerx,centery,direction):
        self.name='fireball'

        frame_rects=[(96,144,8,8),(184,144,8,8),(96,152,8,8),(184,152,8,8),#旋转
                     (112,144,16,16),(112,168,16,16),(112,176,16,16)]#爆炸
        Powerup.__init__(self,centerx,centery,frame_rects,self.name)
        self.name='fireball'
        self.state='fly'
        self.direction=direction
        self.x_vel=10 if self.direction else -10
        self.y_vel=0

        self.timer=0
        gogo(1)



    def update(self,level):
        self.current_time=pygame.time.get_ticks()
        if self.state=='fly':
            self.y_vel=0
            if self.current_time-self.timer>200:
                self.frame_index +=1
                self.frame_index %=4
                self.timer=self.current_time
                self.image=self.frames[self.frame_index]#让火球旋转起来
            self.update_position(level)
        elif self.state=='boom':
            if self.current_time-self.timer>50:
                if self.frame_index<4:
                   self.frame_index+=1
                   self.timer=self.current_time
                   self.image=self.frames[self.frame_index]
                else:
                   self.kill()



    def update_position(self, level):
        self.rect.x += self.x_vel
        self.check_x_collisions(level)
        self.rect.y += self.y_vel
        self.check_y_collision(level)

        if self.rect.x<0 or self.rect.y>C.SCREEN_H:
            self.kill()


    def check_x_collisions(self, level):
        check_group=pygame.sprite.Group(level.ground_items_group,level.enemy_group)
        sprite = pygame.sprite.spritecollideany(self, check_group)
        if sprite:
          self.frame_index=4
          self.state='boom'



    def check_y_collision(self, level):
        check_group = pygame.sprite.Group(level.ground_items_group, level.brick_group)
        sprite = pygame.sprite.spritecollideany(self, check_group)
        if sprite:
            if self.rect.top < sprite.rect.top:
                self.rect.bottom = sprite.rect.top
                self.y_vel = -10#反弹效果


class Slj(Powerup):
    def __init__(self, centerx, centery, direction):
        self.name = 'slj'
        frame_rects = [(84.7,115.9,187,154.5),(291,127.8,153,154),(546.8,139.68,138.2,142.6)]

        Powerup.__init__(self, centerx, centery, frame_rects,self.name)
        self.name = 'slj'
        self.state = 'fly'
        self.direction = direction
        self.x_vel =-10
        self.y_vel = 0
        # centery+=1000
        self.timer = 0


    def update(self, level):
        self.current_time = pygame.time.get_ticks()
        if self.state == 'fly':
            self.y_vel = 0
            if self.current_time - self.timer > 200:
                self.frame_index += 1
                self.frame_index %= 2
                self.timer = self.current_time
                self.image = self.frames[self.frame_index]  # 让火球旋转起来
            self.update_position(level)
        elif self.state == 'boom':
            if self.current_time - self.timer > 50:
                if self.frame_index < 4:
                    self.frame_index += 1
                    self.frame_index %=3
                    self.timer = self.current_time
                    self.image = self.frames[self.frame_index]
                else:
                    self.kill()

    def update_position(self, level):
        self.rect.x += self.x_vel
        self.check_x_collisions(level)
        #self.rect.y += self.y_vel
        #self.check_y_collision(level)

        if self.rect.x < 0 or self.rect.y > C.SCREEN_H:
            self.kill()

    def check_x_collisions(self, level):

        if self.rect.x<=level.player.rect.x:
            self.kill()


    def check_y_collision(self, level):
    
        pass

class LifeMushroon(Powerup):
    pass

class Star(Powerup):
    pass

