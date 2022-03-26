
import pygame
from ..components import info
from .. import setup,tools,sound
from .. import constants as C
from ..components import player,brick,stuff,box,enemy,coin,pipe_and_well
import os
import json

class Level:
    before_buff1_ct = 0
    before_buff2_ct = 0
    curTime = None
    flage=False
    def start(self,game_info):
        self.game_info=game_info#注意这个函数执行顺序是按照这里的初始化的顺序，所有如果定义的话要注意顺序
        self.finished=False
        self.next='game_over'
        self.info=info.Info('level',self.game_info)

        self.load_map_data()
        self.setup_background()
        self.setup_start_position()
        self.setup_player()
        self.setup_bricks_and_boxes()#放在后面检测的前面
        self.setup_ground_items()#实例化
        self.setup_enemies()
        self.check_x_collision()
        self.check_y_collision()
        #self.info = info.Info('level', self.game_info)



        self.setup_checkpoints()


    def load_map_data(self):
        file_name='level_1.json'
        file_path=os.path.join('source/data/maps',file_name)
        with open(file_path) as f:
            self.map_data = json.load(f)
        pygame.mixer.music.load(os.path.abspath("resource/music/main.ogg"))  # 方法问题
        pygame.mixer.music.set_volume(1.0)  # 设置音量
        pygame.mixer.music.play(-1)  # 循环播放

    def setup_background(self):
        self.image_name=self.map_data['image_name']
        self.background = setup.GRAPHICS['level_1.png']
        self.succeed_image=setup.GRAPHICS['succeed.png']
        self.not_succeed_image=setup.GRAPHICS['not_succeed.png']

        self.background_rect = self.background.get_rect()





        rect=self.background.get_rect()
        self.background=pygame.transform.scale(self.background,(int(rect.width*C.LEVEL_H_MULTI),int(rect.height*C.LEVEL_H_MULTI)))


        self.game_window=setup.SCREEN.get_rect()#滑动的游戏窗口 主角不动 窗口滑动
        self.game_ground=pygame.Surface((self.background_rect.width,self.background_rect.height))

    def setup_start_position(self):
        self.position=[]
        for data in self.map_data['maps']:
            self.position.append((data['start_x'],data['end_x'],data['player_x'],data['player_y']))
        self.start_x,self.end_x,self.player_x,self.player_y=self.position[0]

    def setup_player(self):
        self.player=player.Player('mario')
        self.player.rect.x=self.game_window.x + self.player_x#马里奥相对窗口的相对位置
        self.player.rect.bottom=self.player_y

    def setup_ground_items(self):
        self.ground_items_group=pygame.sprite.Group()#多个精灵放入一个组里，方便批量处理，这里和前面不同，之前定义列表，将一个物体xywh坐标放入一个元组再放入列表 这里感觉像一列一列放入的
        for name in ['ground']:#获取json文件中的各个参数
            for item in self.map_data[name]:
                self.ground_items_group.add(stuff.Item(item['x'],item['y'],item['width'],item['height'],name))#将参数传入stuff中的Item大类，这个group可能只能接受这种


    def setup_bricks_and_boxes(self):
        self.brick_group=pygame.sprite.Group()
        #self.box_group=pygame.sprite.Group()
        self.coin_sentence_group=pygame.sprite.Group()
        self.powerup_group=pygame.sprite.Group()
        self.pipe_and_well_group=pygame.sprite.Group()
        self.coin_buff1_group=pygame.sprite.Group()
        self.coin_buff2_group = pygame.sprite.Group()
        self.coin_before_buff1_group=pygame.sprite.Group()
        self.coin_before_buff2_group=pygame.sprite.Group()


        if 'brick' in self.map_data:
            for brick_data in self.map_data['brick']:
                x,y=brick_data['x'],brick_data['y']
                brick_type=brick_data['type']
                if brick_type==0:
                    if 'brick_num' in brick_data:#如果是批量处理
                        #TODO BATCH bricks
                        pass
                    else:
                        self.brick_group.add(brick.Brick(x,y,brick_type,None))#add应该就是添加class的这种
                #elif brick_type==1:
                #    self.brick_group.add(brick.Brick(x,y,brick_type,self.coin_group))
                else:
                    self.brick_group.add(brick.Brick(x,y,brick_type,self.powerup_group))


        #if 'box' in self.map_data:
        #    for box_data in self.map_data['box']:
         #       x, y = box_data['x'], box_data['y']
          #      box_type = box_data['type']
          #      if box_type == 1:
           #         self.box_group.add(box.Box(x, y, box_type,self.coin_group))
           #     else:
           #         self.box_group.add(box.Box(x,y,box_type,self.powerup_group))

        if 'words' in self.map_data:
            for coin_data in self.map_data['words']:
                x,y,type,group=coin_data['x'],coin_data['y'],coin_data['type'],coin_data['group']
                if group==0:
                    self.coin_sentence_group.add(coin.Coin(x,y,type,group))
                elif group==1 and type!=3:
                    self.coin_before_buff1_group.add(coin.Coin(x,y,type,group))
                elif group == 2 and type != 3:
                    self.coin_before_buff2_group.add(coin.Coin(x, y, type, group))
                elif group==1 and type==3:
                    self.coin_buff1_group.add(coin.Coin(x,y,type,group))
                elif group==2 and type==3:
                    self.coin_buff2_group.add(coin.Coin(x,y,type,group))

        if 'pipe_and_well' in self.map_data:
            for pipe_data in self.map_data['pipe_and_well']:
                x,y,pipe_and_well_type=pipe_data['x'],pipe_data['y'],pipe_data['type']

                self.pipe_and_well_group.add(pipe_and_well.Pipe_and_well(x,y,pipe_and_well_type,None))


    def setup_enemies(self):
        self.dying_group=pygame.sprite.Group()
        self.enemy_group=pygame.sprite.Group()
        self.shell_group=pygame.sprite.Group()
        self.enemy_group_dict={}
        self.small_house_group=pygame.sprite.Group()


        for enemy_group_data in self.map_data['enemy']:
            group=pygame.sprite.Group()
            for enemy_group_id,enemy_list in enemy_group_data.items():
                for enemy_data in enemy_list:
                    group.add(enemy.create_enemy(enemy_data))
                self.enemy_group_dict[enemy_group_id]=group

    def setup_checkpoints(self):
        self.checkpoint_group=pygame.sprite.Group()
        for item in self.map_data['checkpoint']:
            x,y,w,h=item['x'],item['y'],item['width'],item['height']
            checkpoint_type=item['type']
            enemy_groupid=item.get('enemy_groupid')
            self.checkpoint_group.add(stuff.Checkpoint(x,y,w,h,checkpoint_type,enemy_groupid))


    def update(self,surface,keys):#调用玩家的更新方法 将键盘动作传入

        self.player.update(keys,self)#自身self就是level

        if self.player.dead:
            if pygame.time.get_ticks()-self.player.death_timer>3000:#获取当前时间 死了三秒以上则结束游戏
                self.finished=True
                self.update_game_info()
        elif self.is_frozen():
            pass
        else:
            self.update_player_position()
            self.check_checkpoints()
            self.check_if_go_die()
            self.update_game_window()
            #self.succeed()
            self.info.update()
            self.brick_group.update()
            self.enemy_group.update(self)
            self.dying_group.update(self)
            self.shell_group.update(self)
            self.coin_sentence_group.update()
            self.coin_before_buff1_group.update()
            self.coin_before_buff2_group.update()
            self.coin_buff1_group.update()
            self.coin_buff2_group.update()

            self.powerup_group.update(self)  # 将level实例传给这个函数




        self.draw(surface)
        #self.info.update(surface)

    def update_player_position(self):#用当前玩家的速度更新玩家的位置
        # x direction
        self.player.rect.x += self.player.x_vel
        if self.player.rect.x<self.start_x:
            self.player.rect.x=self.start_x
        elif self.player.rect.right>self.end_x:
            self.player.rect.right=self.end_x
        self.check_x_collision()
        print(self.player.rect.x,'    ',self.player.rect.y)
        #if self.player.rect.x<0:#防止人物跑出屏幕外面吧
        #    self.player.rect.x=0
        #if self.player.rect.x>C.SCREEN_W-16*C.PLAYER_MULTI:
        #    self.player.rect.x=C.SCREEN_W-16*C.PLAYER_MULTI

        #y direction
        if not  self.player.dead:#如果马里奥死亡不需要进入后续的下落地面检测
            self.player.rect.y +=self.player.y_vel
            self.check_y_collision()

    def check_x_collision(self):#果然这里检测的思路统一比较x坐标 传入的时候则不能用最开始使用的传入方法
        check_group=pygame.sprite.Group(self.ground_items_group,self.brick_group)#在合一个大的组

        collided_sprite=pygame.sprite.spritecollideany(self.player,check_group)#返bool值
        if collided_sprite:#如果碰撞即true
            self.adjust_player_x(collided_sprite)

        if self.player.hurt_immune:
            return #如果伤害免疫跳过后面代码

        enemy = pygame.sprite.spritecollideany(self.player, self.enemy_group)
        if enemy:
            if self.player.big:
                self.player.state='big2small'
                self.player.hurt_immune=True
            else:
                self.player.go_die()


        shell=pygame.sprite.spritecollideany(self.player,self.shell_group)
        if shell:
            if self.player.rect.x<shell.rect.x:
                shell.x_vel=10
                shell.rect.x+=40#直接反弹
                shell.direction=1
            else:
                shell.x_vel=-10
                shell.rect.x-=40
                shell.direction=0
            shell.state='slide'
        powerup=pygame.sprite.spritecollideany(self.player,self.powerup_group)
        if powerup:
            if powerup.name=='slj':
                if self.player.big:
                    self.player.state = 'big2small'
                    self.player.hurt_immune = True
                else:
                    self.player.go_die()
                    powerup.kill()
            if powerup.name=='mushroom':
                self.player.state='small2big'
                powerup.kill()



        before_buff1=pygame.sprite.spritecollideany(self.player,self.coin_before_buff1_group)
        if before_buff1:
            self.before_buff1_ct+=1
            self.game_info['num'] += 1
            before_buff1.kill()
        buff1=pygame.sprite.spritecollideany(self.player,self.coin_buff1_group)

        if  buff1 and self.before_buff1_ct==3:
            self.game_info['num'] += 1
            self.player.state='small2big'
            buff1.kill()

        before_buff2 = pygame.sprite.spritecollideany(self.player, self.coin_before_buff2_group)
        if before_buff2:
            self.before_buff2_ct += 1
            self.game_info['num']+=1
            before_buff2.kill()
        buff2 = pygame.sprite.spritecollideany(self.player, self.coin_buff2_group)

        if buff2 and self.before_buff2_ct == 3:
            self.game_info['num'] += 1
            self.player.state = 'small2big'
            buff2.kill()



        pipe_and_well=pygame.sprite.spritecollideany(self.player,self.pipe_and_well_group)
        if pipe_and_well:
            self.adjust_player_x(pipe_and_well)





    def check_y_collision(self):
        ground_item=pygame.sprite.spritecollideany(self.player,self.ground_items_group)
        brick=pygame.sprite.spritecollideany(self.player,self.brick_group)
        #box=pygame.sprite.spritecollideany(self.player,self.box_group)
        enemy=pygame.sprite.spritecollideany(self.player,self.enemy_group)

        if brick :
            self.adjust_player_y(brick)

        pipe_and_well = pygame.sprite.spritecollideany(self.player, self.pipe_and_well_group)
        if pipe_and_well:
            self.adjust_player_y(pipe_and_well)

        word=pygame.sprite.spritecollideany(self.player,self.coin_sentence_group)
        if word:

            self.game_info['num']+=1
            word.kill()



        #collided_sprite = pygame.sprite.spritecollideany(self.player, check_group)  # 返bool值
        #if collided_sprite:  # 如果碰撞即true
        #    self.adjust_player_y(collided_sprite)
        if ground_item:
            self.adjust_player_y(ground_item)
        elif brick:
            self.adjust_player_y(brick)
       #elif box:
        #    self.adjust_player_y(box)
        elif enemy:
            if self.player.hurt_immune:
                return
            self.enemy_group.remove(enemy)#由敌人组进入死亡组
            if enemy.name=='koopa':
                self.shell_group.add(enemy)#入龟壳组
            else:
                self.dying_group.add(enemy)

            if self.player.y_vel<0:
                how='bumped'
            else:
                how='trampled'
                self.player.state='jump'
                self.player.rect.bottom=enemy.rect.top
                self.player.y_vel=self.player.jump_vel*0.8

            enemy.go_die(how,1 if self.player.face_right else -1)

        self.check_will_fall(self.player)



    def adjust_player_x(self,sprite):
        if self.player.rect.x<sprite.rect.x:#也就是碰上去弹回来
            self.player.rect.right=sprite.rect.left
        else:
            self.player.rect.left=sprite.rect.right

        self.player.x_vel=0

    def adjust_player_y(self,sprite):
        #downwards
        if self.player.rect.bottom<sprite.rect.bottom:
            self.player.y_vel=0
            self.player.rect.bottom=sprite.rect.top
            self.player.state='walk'
        #upwards
        else:
            self.player.y_vel=7
            self.player.rect.top=sprite.rect.bottom#反弹效果
            self.player.state='fall'

            self.is_enemy_on(sprite)

            #if sprite.name=='box':
            #    if sprite.state=='rest':
            #        sprite.go_bumped()

            #if sprite.name=='brick':
            #    if self.player.big and sprite.brick_type==0:#变大状态且是空砖块
            #        sprite.smashed(self.dying_group)
            #    else:
            sprite.go_bumped()

    def is_enemy_on(self,sprite):
        sprite.rect.y-=1#假意使砖块向上靠，如果有发生触碰，则有敌人
        enemy=pygame.sprite.spritecollideany(sprite,self.enemy_group)
        if enemy:
            self.enemy_group.remove(enemy)
            self.dying_group.add(enemy)
            if sprite.rect.centerx>enemy.rect.centerx:
                enemy.go_die('bumped',-1)
            else:
                enemy.go_die('bumped',1)
        sprite.rect.y+=1

    def check_will_fall(self,sprite):
        sprite.rect.y+=1
        check_group=pygame.sprite.Group(self.ground_items_group,self.brick_group)
        collided_sprite=pygame.sprite.spritecollideany(sprite,check_group)
        if not collided_sprite and sprite.state!='jump' and not self.is_frozen():
            sprite.state='fall'
        sprite.rect.y-=1

    #def succeed(self):

     #   if self.player.rect.x > 15200 and self.game_info['num'] == 20:

            #self.background.blit(self.succeed_image, (200, 300))
            #if pygame.mouse.get_pressed() == (1, 0, 0):
            #    pygame.time.wait(500)
     #           self.game_info['num']=0
      #          self.finished = True
       #         self.next = 'end'
       # elif self.player.rect.x > 15200 and self.game_info['num'] != 20:
            #print("ok")
            #self.game_info['num'] = 0
            #self.game_info['player_state']=1
            #self.finished=True
            #self.next='end'
        #    self.background.blit(self.not_succeed_image, (0, 0))
            #if pygame.mouse.get_pressed() == (1, 0, 0):
            #    self.setup_background()

            #self.flage=True



    def update_game_window(self):
        self.start_x = self.game_window.x
        #second=self.game_window.x + self.game_window.width/2#计算出窗口的三分之一位置
        # if self.player.x_vel>0 and self.player.rect.centerx > second :
        #self.game_window.x+=self.player.x_vel#按马里奥的速度移动这个窗口
        if  self.player.rect.centerx>500:
            self.game_window.x += self.player.x_vel


        # self.start_x=self.game_window.x+500

        #if self.game_window.x <-500:
        #    self.player.x_vel=10

    def draw(self,surface):
        self.game_ground.blit(self.background,self.game_window,self.game_window)#背景和窗口都绘制到ground里面
        self.game_ground.blit(self.player.image,self.player.rect)#人物也绘制进去
        #self.game_ground.blit(self.count_word,(10,55))
        self.powerup_group.draw(self.game_ground)#改变绘制顺序，才能有蘑菇长出来的效果
        self.brick_group.draw(self.game_ground)#绘制砖块
        self.enemy_group.draw(self.game_ground)
        self.dying_group.draw(self.game_ground)
        self.shell_group.draw(self.game_ground)
        self.coin_sentence_group.draw(self.game_ground)
        self.coin_before_buff1_group.draw(self.game_ground)
        self.coin_before_buff2_group.draw(self.game_ground)
        self.coin_buff1_group.draw(self.game_ground)
        self.coin_buff2_group.draw(self.game_ground)
        self.pipe_and_well_group.draw(self.game_ground)
        self.info.draw(surface)
        #if self.succeed()==1:
        #    self.game_ground.blit(self.succeed_image,(200,300))
        #if self.succeed()==2:
        #    print("ok")
        #    surface.blit(setup.GRAPHICS['not_succeed.png'], (15306, 300))
        #    surface.blit(setup.GRAPHICS['not_succeed.png'], (300, 300))
        #    pygame.display.flip()
        #    pygame.display.update()
        #    surface.blit(setup.GRAPHICS['not_succeed.png'], (15306, 300))
        #    surface.blit(setup.GRAPHICS['not_succeed.png'], (300, 300))
        #self.count_word.draw(surface)

        surface.blit(self.game_ground,(0,0),self.game_window)#第一个参数代表目标图层，第三个参数代表指定位置 中间就是放入的左上角
        self.info.draw(surface)
        if self.player.rect.x > 15200 and self.game_info['num'] == 21:
            surface.blit(self.succeed_image,(0,0))
            if self.curTime == None:
               self.curTime = pygame.time.get_ticks()
            if self.curTime != None:
                if pygame.time.get_ticks() - self.curTime > 3000:
                    self.finished=True
                    self.next='body_title'
        elif self.player.rect.x > 15200 and self.game_info['num'] != 21:

           surface.blit(self.not_succeed_image, (0, 0))


    def check_checkpoints(self):
        checkpoint=pygame.sprite.spritecollideany(self.player,self.checkpoint_group)
        if checkpoint:
            if checkpoint.checkpoint_type==0:
                self.enemy_group.add(self.enemy_group_dict[str(checkpoint.enemy_groupid)])
            checkpoint.kill()#检查点被触碰就消失

    def check_if_go_die(self):
        if self.player.rect.y>C.SCREEN_H:#判断马里奥是否掉出屏幕外
            self.player.go_die()

    def update_game_info(self):
        if self.player.dead:
            self.next='ask'
            #self.game_info['lives']-=1
       # if self.game_info['lives']==0:
        #    self.next='game_over'
        #else:
        #    self.next='load_screen'

    def is_frozen(self):
        return self.player.state in ['small2big','big2small','big2fire','fire2small']

