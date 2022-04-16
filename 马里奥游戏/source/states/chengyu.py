import pygame
from .. import setup  # ..是上一级文件
import os
from .. import tools
from .. import constants as C
from ..components import info  # 到上一级目录平行的components
import random

def gogo(num):
    if num==1:
        fii='eat.ogg'
    elif num==2:
        fii='drop.ogg'
    abs = os.getcwd()
    sds = abs.split(r'\\')
    ewr = sds[0] + r'\\resource\\music\\'+fii
    try:
        pygame.mixer.Sound(ewr).play()
    except:
        ewr = sds[0].split('dist') + r'resource\\music\\' + fii
        pygame.mixer.Sound(ewr).play()
    return 0


class Chengyu:
    instance = None
    flag = False
    ct = 0

    def __init__(self):
        game_info = {
            'score': 0,
            'coin': 0,
            'lives': 3,
            'player_state': 'small'  # 大的还是小的什么的

        }
        self.start(game_info)

    def start(self, game_info):
        self.background = setup.GRAPHICS['ditu.png']
        self.index = 0
        self.background_rect = self.background.get_rect()
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))

        self.game_info = game_info
        self.time = pygame.time.get_ticks()


        self.FPS = 60  # 帧切换的时间间隔
        self.window_width = 1200  # 开的游戏屏幕宽度
        self.window_height = 900  # 开的屏幕高度
        self.reveal_speed = 8  # 方块揭开合上的速度
        self.box_size = 100  # 方块的长和宽
        self.gap_size = 30  # 方块间隔的长
        self.board_width_count = 5  # 横着方块的个数
        self.board_height_count = 2  # 竖着的方块个数

        # assert (board_width_count * board_height_count) % 2 == 0  # 需要总的个数是偶数
        self.x_margin = int((self.background_rect.width - (self.board_width_count) * (
                    self.box_size + self.gap_size)) / 2) + 200  # 在背景中开始画上方块的x坐标
        self.y_margin = int((self.background_rect.height - (
                    self.board_height_count * (self.box_size + self.gap_size))) / 2) + 200  # 在背景中开始画上方块的y坐标

        # 游戏所涉及到的颜色
        self.gray = (100, 100, 100)  # 灰
        self.navyblue = (60, 60, 100)  # 灰蓝
        self.white = (255, 255, 255)  # 白

        self.blue = (0, 0, 255)  # 蓝色

        self.bg_color = self.navyblue  # 背景颜色
        self.light_bg_color = self.gray
        self.box_color = self.white  # 未翻开的方块颜色
        self.high_light_color = (100,0,0)  # 高光颜色


        self.fps_clock = pygame.time.Clock()

        self.mouse_x = 0  # 默认开始鼠标位置
        self.mouse_y = 0
        pygame.display.set_caption('汉字记忆小游戏')

        self.mainBoard = self.get_Randomized_Board()
        self.revealedBoxes = self.generate_Revealed_Boxes_Data(False)

        self.first_Selection = None  # 记录第一个被点击的方块的（x，y）

        # 背景被填充为前面设置的背景色


        self.icons = [(setup.GRAPHICS['pin_1.png'], 1), (setup.GRAPHICS['pin_2.png'], 2),
                      (setup.GRAPHICS['pin_3.png'], 3), (setup.GRAPHICS['pin_4.png'], 4),
                      (setup.GRAPHICS['zi_1.png'], 1), (setup.GRAPHICS['zi_2.png'], 2),
                      (setup.GRAPHICS['zi_3.png'], 3), (setup.GRAPHICS['zi_4.png'], 4),
                      (setup.GRAPHICS['pin_5.png'], 5), (setup.GRAPHICS['zi_5.png'], 5)]

        random.shuffle(self.icons)  # 将列表顺序打乱
        self.board = []
        for x in range(self.board_width_count):
            column = []  # 列
            for y in range(self.board_height_count):
                column.append(self.icons[0])  # 虽然每次都添加的是icons的第一个形状，但是添加完之后删除，所以，没有重复添加
                del self.icons[0]  #
            self.board.append(column)
        self.finished = False
        self.next = 'chuangguan'

    def generate_Revealed_Boxes_Data(self, val):
        revealedBoxes = []
        for i in range(self.board_width_count):
            revealedBoxes.append([val] * self.board_height_count)
        return revealedBoxes

    def get_Randomized_Board(self):  # 得到随机所有形状
        pass

    def split_Into_Group_Of(self, groupSize, theList):
        result = []
        for i in range(0, len(theList), groupSize):
            result.append(theList[i:i + groupSize])
        return result

    def left_Top_Coord_Of_Box(self, box_x, box_y):  # 得到方块的左上角坐标,传入的是这个方块在这个矩阵的第几行第几个
        left = box_x * (self.box_size + self.gap_size) + self.x_margin
        top = box_y * (self.box_size + self.gap_size) + self.y_margin
        return (left, top)

    def get_Box_At_Pixel(self, x, y):  # 得到方块在矩阵中的位置
        for box_x in range(self.board_width_count):
            for box_y in range(self.board_height_count):
                left, top = self.left_Top_Coord_Of_Box(box_x, box_y)
                boxRect = pygame.Rect(left, top, self.box_size, self.box_size)
                if boxRect.collidepoint(x, y):
                    return (box_x, box_y)
        return (None, None)

    def draw_Icon(self, box, box_x, box_y):

        left, top = self.left_Top_Coord_Of_Box(box_x, box_y)  # 这里面画都是直接画出形状

        self.background.blit(box, (left - 200, top - 200))

    def get_Shape_And_Color(self, box_x, box_y):
        return self.board[box_x][box_y][0], self.board[box_x][box_y][1]  # 分别是shape和color

    def draw_Box_Covers(self, board, box, coverage):
        left, top = self.left_Top_Coord_Of_Box(box[0][0], box[0][1])

        shape, type = self.get_Shape_And_Color(box[0][0], box[0][1])
        if coverage < 0:
            self.draw_Icon(shape, box[0][0], box[0][1])  # 将方块画上去
        if coverage > 0:  #
            self.background.blit(self.cover_image, (left - 200, top - 215))

        pygame.display.update()
        self.fps_clock.tick(self.FPS)

    def reveal_Boxes_Animation(self, board, boxes_To_Reveal):  # 展开动画
        self.draw_Box_Covers(board, boxes_To_Reveal, -1)

    def cover_Boxes_Animation(self, board, boxes_To_Cover):
        self.draw_Box_Covers(board, boxes_To_Cover, 1)  # 中间参数是要进行盖上的方块

    def draw_Board(self, board, revealed):
        for box_x in range(self.board_width_count):
            for box_y in range(self.board_height_count):
                left, top = self.left_Top_Coord_Of_Box(box_x, box_y)
                if not revealed[box_x][box_y]:  # 如果不是要展开的，则画上覆盖方块
                    self.cover_image=setup.GRAPHICS['cover.png']
                    self.background.blit(self.cover_image, (left - 200, top - 215))
                else:
                    shape, type = self.get_Shape_And_Color(box_x, box_y)  # 如果是要展开的则画上对应形状
                    self.draw_Icon(shape, box_x, box_y)

    def draw_Highlight_Box(self, box_x, box_y):
        left, top = self.left_Top_Coord_Of_Box(box_x, box_y)

        pygame.draw.line(self.background, self.high_light_color,
                         (left-200,top+100-200+10) ,(left+115-5-200,top+100-200+10), 8)  # 画在方块外面


    def update(self, surface, keys):

        surface.blit(self.background, (200, 200))

        self.draw_Board(self.mainBoard, self.revealedBoxes)  # 不断画游戏界面,主要背景和方块
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.mouseClicked = pygame.mouse.get_pressed()

        box_x, box_y = self.get_Box_At_Pixel(self.mouse_x, self.mouse_y)  # pixel像素 获取鼠标放在的方块在矩阵当中的位置
        if box_x != None and box_y != None:  #
            # 当鼠标此时放在方块上时
            self.draw_Highlight_Box(box_x, box_y)  # 将这个方块标亮

            if not self.revealedBoxes[box_x][box_y] and self.mouseClicked == (1, 0, 0):  # 如果不是打开的并且鼠标点击了，则再打开
                gogo(2)
                shape, type = self.get_Shape_And_Color(box_x, box_y)
                self.draw_Icon(shape, box_x, box_y)
                # self.draw_Board(self.mainBoard, self.revealedBoxes)
                self.revealedBoxes[box_x][box_y] = True  # 将这个方块打开
                if self.first_Selection == None:  # 如果第一个方块还未被选出
                    self.first_Selection = (box_x, box_y)  # 则这就是第一个方块
                else:# 如果是第二个方块被点击
                    #检查和第一个方块是否匹配
                    icon1_shape, icon1_type = self.get_Shape_And_Color(self.first_Selection[0], self.first_Selection[1])
                    icon2_shape, icon2_type = self.get_Shape_And_Color(box_x, box_y)
                    if icon1_type != icon2_type:
                        self.cover_Boxes_Animation(self.mainBoard, [(self.first_Selection[0], self.first_Selection[1]),
                                                                    (box_x, box_y)])  #将这个方块盖上
                        self.revealedBoxes[self.first_Selection[0]][self.first_Selection[1]] = False  # 将打开第一个方块状态置为false
                        self.revealedBoxes[box_x][box_y] = False  #将打开的第二个方块置为false
                    elif icon2_type == icon1_type:
                        print('good')
                        # shape, type = self.get_Shape_And_Color(box_x, box_y)
                        #self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))
                        left, top = self.left_Top_Coord_Of_Box(box_x, box_y)
                        left_1, top_1 = self.left_Top_Coord_Of_Box(self.first_Selection[0],  self.first_Selection[1])
                        #surface.blit(setup.GRAPHICS['bamboo.png'], (left, top))
                        #surface.blit(setup.GRAPHICS['bamboo.png'], (left_1, top_1))
                        self.revealedBoxes[self.first_Selection[0]][self.first_Selection[1]] = True  # 将打开第一个方块状态置为false
                        self.revealedBoxes[box_x][box_y] =True
                        self.first_Selection = None

                        if self.ct >= 4 and pygame.mouse.get_pressed()==(1,0,0):
                            pygame.time.wait(500)
                            self.finished = True
                            self.next = 'chuangguan'
                        self.ct += 1
        # 将第一个方块置为没有
    def draw(self,surface):
        box_x, box_y = self.get_Box_At_Pixel(self.mouse_x, self.mouse_y)  # pixel像素 获取鼠标放在的方块在矩阵当中的位置
        if box_x != None and box_y != None:
            self.draw_Highlight_Box(box_x, box_y)
        pygame.display.flip()



