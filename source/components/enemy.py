

import pygame
from .. import setup,tools
from ..components import powerup
from .. import constants as C
from ..states import level,level2,level3
def create_enemy(enemy_data):
    enemy_type=enemy_data['type']
    x,y_bottom,direction,color=enemy_data['x'],enemy_data['y'],enemy_data['direction'],enemy_data['color']#注意这里y是底部的y

    if enemy_type==0:#normal_enemy

        enemy=normal_enemy(x,y_bottom,direction,'goomba',color)
    elif enemy_type==1:#special_enemy
        enemy=special_enemy(x,y_bottom,direction,'koopa',color)

    return enemy

class Enemy(pygame.sprite.Sprite):
    ct=0
    def __init__(self,x,y_bottom,direction,name,frame_rects):
        pygame.sprite.Sprite.__init__(self)
        self.direction=direction
        self.name=name
        self.frame_index=0
        self.left_frames=[]
        self.right_frames=[]

        self.load_frames(name,frame_rects)
        self.frames=self.left_frames if self.direction==0 else self.right_frames
        self.image =self.frames[self.frame_index]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.bottom=y_bottom

        self.timer=0
        self.x_vel=-1*C.ENEMY_SPEED if self.direction==0 else C.ENEMY_SPEED#让敌人左右机械移动
        self.y_vel=0
        self.gravity=C.GRAVITY
        self.state='walk'
        self.can_shoot = True


    def load_frames(self,name,frame_rects):
        if name=='goomba':#normal
                self.left_frames=[setup.GRAPHICS['n_enemy_1.png'],setup.GRAPHICS['n_enemy_2.png'],setup.GRAPHICS['n_enemy_3.png'],setup.GRAPHICS['n_enemy_6.png'],setup.GRAPHICS['n_enemy_7.png']]
                self.right_frames=[pygame.transform.flip(setup.GRAPHICS['n_enemy_1.png'],True,False),
                                   pygame.transform.flip(setup.GRAPHICS['n_enemy_2.png'],True,False),
                                   pygame.transform.flip(setup.GRAPHICS['n_enemy_3.png'],True,False),
                                   pygame.transform.flip(setup.GRAPHICS['n_enemy_6.png'],True,False),
                                   pygame.transform.flip(setup.GRAPHICS['n_enemy_7.png'],True,False)]
        if name=='koopa':

                self.left_frames=[setup.GRAPHICS['enemy1.png'],setup.GRAPHICS['enemy2.png'],setup.GRAPHICS['enemy3.png'],setup.GRAPHICS['enemy6.png'],setup.GRAPHICS['n_enemy_7.png']]
                self.right_frames = [pygame.transform.flip(setup.GRAPHICS['enemy1.png'], True, False),
                                     pygame.transform.flip(setup.GRAPHICS['enemy2.png'], True, False),
                                     pygame.transform.flip(setup.GRAPHICS['enemy3.png'], True, False),
                                     pygame.transform.flip(setup.GRAPHICS['enemy6.png'], True, False),
                                     pygame.transform.flip(setup.GRAPHICS['n_enemy_7.png'], True, False)]

    def update(self,level):
        self.current_time=pygame.time.get_ticks()
        self.handle_states(level)
        self.update_position(level)

    def handle_states(self,level):

        if self.state=='walk':#也就是到哪个状态用调哪个函数
            self.walk()
        elif self.state=='fall':
            self.fall()
        elif self.state=='die':
            self.die()
        elif self.state=='trampled':
            self.trampled(level)
        elif self.state=='slide':
            self.slide()
        elif self.state=='hurt':
            self.hurt(level)

        if self.direction:
            self.image=self.right_frames[self.frame_index]
        else:
            self.image=self.left_frames[self.frame_index]

    def can_shoot_or_not(self, level):
        if self.rect.x-level.player.rect.x>900:
            self.can_shoot = True

    def walk(self):
        if self.current_time-self.timer>125:
            self.frame_index=(self.frame_index+1)%3
            self.image=self.frames[self.frame_index]
            self.timer=self.current_time

    def fall(self):
        if self.y_vel<10:
            self.y_vel+=self.gravity

    def die(self):

        self.frame_index = 3
        self.image = self.frames[self.frame_index]

        if self.current_time - self.death_timer > 80:
            self.kill()
    def hurt(self,level):

        self.frame_index=4
        self.image=self.frames[self.frame_index]
        if self.current_time - self.death_timer > 100:
            self.state='walk'


    def trampled(self,level):
        pass

    def slide(self):
        pass

    def update_position(self,level):
        self.rect.x += self.x_vel
        self.check_x_collisions(level)
        self.rect.y += self.y_vel
        if self.state!='die':
             self.check_y_collision(level)

    def check_x_collisions(self,level):
        sprite=pygame.sprite.spritecollideany(self,level.ground_items_group)
        if sprite:
            self.direction=1 if self.direction==0 else 0
            if self.direction:#向右#这里主要是龟壳碰撞希望回来
                self.direction=0
                self.rect.right=sprite.rect.left
            else:
                self.direction=1
                self.rect.left=sprite.rect.right
            self.x_vel*=-1

        powerup=pygame.sprite.spritecollideany(self,level.powerup_group)
        if powerup:

            if powerup.name=='fireball' and level.player.big!=True:
                self.ct+= 1
                self.death_timer=self.current_time
                if self.ct==2:
                    self.state='die'
                else:
                    self.state='hurt'
                powerup.kill()

            if powerup.name == 'fireball' and level.player.big != False:
                self.death_timer = self.current_time
                self.state='die'
                powerup.kill()
        if self.rect.x-level.player.rect.x<600 and self.can_shoot==True :

            self.shoot_slj(level)
            self.can_shoot=False



        if self.state=='slide':
            enemy=pygame.sprite.spritecollideany(self,level.enemy_group)
            if enemy:
                enemy.go_die(how='slide',direction=self.direction)
                level.enemy_group.remove(enemy)
                level.dying_group.add(enemy)

    def check_y_collision(self,level):
        check_group=pygame.sprite.Group(level.ground_items_group,level.brick_group)
        sprite=pygame.sprite.spritecollideany(self,check_group)
        if sprite:
            if self.rect.top<sprite.rect.top:
                self.rect.bottom=sprite.rect.top
                self.y_vel=0
                self.state='walk'
        level.check_will_fall(self)

    def go_die(self,how,direction=1):
        pass
    def shoot_slj(self,level):

        slj = powerup.Slj(self.rect.centerx, self.rect.centery, -1)  # 火球是pygame中的精灵
        level.powerup_group.add(slj)  # 把发射火球这个方法传入level中的这个组中


class normal_enemy(Enemy):#normal
    def __init__(self,x,y_bottom,direction,name,color):

        self.frame_rects=[(337,229,436,1012),(1143,229,418,1008),(2407,225,576,1008),(2407,225,576,1008),(3240,243,526,1003),(3946,360,634,855)]
        Enemy.__init__(self,x,y_bottom,direction,name,self.frame_rects)

    def trampled(self,level):
        self.x_vel=0
        self.frame_index=2
        if self.death_timer==0:
            self.death_timer=self.current_time
        if self.current_time - self.death_timer>500:
            self.kill()


class special_enemy(Enemy):#乌龟 都继承敌人类
    def __init__(self, x, y_bottom, direction, name, color):
        self.frame_rects=[(337,229,436,1012),(1143,229,418,1008),(2407,225,576,1008),(2407,225,576,1008),(3240,243,526,1003),(3946,360,634,855)]
        Enemy.__init__(self,x, y_bottom, direction, name,self.frame_rects)
        self.shell_timer=0

    def trampled(self,level):
        self.x_vel=0
        self.frame_index=2#缩头乌龟
        if self.shell_timer==0:
            self.shell_timer=self.current_time
        if self.current_time-self.shell_timer>5000:
            self.state='walk'
            self.x_vel=-C.ENEMY_SPEED if self.direction==0 else C.ENEMY_SPEED
            level.enemy_group.add(self)
            level.shell_group.remove(self)#钻出来之后又变成敌人组
            self.shell_timer=0

    def slide(self):
        pass


