import pygame
import  os
# 初始化
pygame.init()

# 創建視窗
WIDTH = 1000
HIGH = 1000
SCREEN = pygame.display.set_mode((WIDTH, HIGH))

# 標題
pygame.display.set_caption('SpaceWarrrrr')
pygame.display.set_caption('SpaceWarrrrr')

# 時間管理
clock = pygame.time.Clock()

# 遊戲幀數
FPS = 60

# 射擊間隔
psi = 20
pirate_ship_psi = 80
boss_psi = 10

# 遊戲狀態
running = True

# 分數
score = 0

# 各類顏色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 97, 0)
BLACK = (0, 0, 0)
# 字體載入
font_name = os.path.join("font.ttf")


# 敵人參數
ps_count = 1
ps_damage = 0
