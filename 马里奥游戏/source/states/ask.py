import pygame
from .. import setup  # ..是上一级文件
from .. import tools
from .. import constants as C
from ..components import info  # 到上一级目录平行的components
import random


class Ask:
    instance = None
    expanded_i = 1

    def __init__(self):
        game_info = {
            'score': 0,
            'coin': 0,
            'lives': 3,
            'player_state': 'small'  # 大的还是小的什么的

        }
        self.start(game_info)

    def start(self, game_info):
        self.game_info = game_info

        self.ask0 = setup.GRAPHICS['paint_1.png']
        self.ask1 = setup.GRAPHICS['paint_2.png']
        self.ask2 = setup.GRAPHICS['paint_3.png']
        self.yes = setup.GRAPHICS['bamboo.png']

        # self.ask6 = setup.GRAPHICS['ask_6.png']
        self.frames = [self.ask0, self.ask1, self.ask2]
        self.answer_rects = [(0, 0, 100, 100), (100, 100, 200, 200), (200, 200, 300, 300), (300, 300, 400, 400)]
        self.answer_dict = {'0': 1,
                            '1': 2,
                            '2': 0}

        self.setup_background()

        self.finished = False  # 只要这个阶段还在运行就不完结
        self.next = 'load_screen'

    def setup_background(self):  # 设置底图\\
        self.num = random.randint(0, 2)
        print(self.num)
        self.background = self.frames[self.num]  #
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (
            int(self.background_rect.width * C.BG_W_MULTI), int(self.background_rect.height * C.BG_H_MULTI)))
        self.viewport = setup.SCREEN.get_rect()  # 滑动窗口
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))

    curTime = None

    def update(self, surface, keys):  # 更新操作

        surface.blit(self.background, self.background_rect)
        # check_0= tools.button(*self.answer_rects[0])#检查各个选项
        # check_1= tools.button(*self.answer_rects[1])

        # check_2= tools.button(*self.answer_rects[2])
        # check_3= tools.button(*self.answer_rects[3])
        self.answer = self.answer_dict[str(self.num)]  # 记录正确答案对应的选项
        print(self.answer)
        check_right = tools.button(*self.answer_rects[self.answer])
        print(*self.answer_rects[self.answer])
        print(check_right)
        self.time = pygame.time.get_ticks()

        if self.curTime!=None:
            if pygame.time.get_ticks() - self.curTime > 3000:
                # pygame.time.delay(3000)
                self.finished = True
                self.next = 'level'
                self.curTime = None
        if check_right == 8:
            self.background.blit(self.yes, self.background_rect)
            if self.curTime == None:
                self.curTime = pygame.time.get_ticks()

        elif check_right == 6:
            self.finished = True
            self.next = 'main_menu'

    def draw(self, surface):
        self.game_ground.blit(self.background, (0, 0))
