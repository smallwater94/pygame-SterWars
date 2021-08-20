from maineed.setting import *


def add_img(file, filename):
    return pygame.image.load(os.path.join(file, filename)).convert()


def add_sound(file, filename):
    return pygame.mixer.Sound(os.path.join(file, filename))


def set_size(png, size):
    return pygame.transform.scale(png, (size, size))


def set_size_X_Y(png, xsize, ysize):
    return pygame.transform.scale(png, (xsize, ysize))


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 200
    BAR_HIGHT = 15
    fill = (hp / 100) * BAR_LENGTH
    outline_recy = pygame.Rect(x, y, BAR_LENGTH, BAR_HIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, GREEN, outline_recy, 2)

def drow_init():
    draw_text(SCREEN, '太空生存戰', 128, 500, 200)
    draw_text(SCREEN, 'W A S D 控制方向', 64, 500, 400)
    draw_text(SCREEN, '藍色船打爆生成道具，關底有Boss', 48, 500, 500)
    draw_text(SCREEN, '音樂用心找，可以聽聽，嘔對 可能會很大聲', 48, 500, 600)
    draw_text(SCREEN, '[按下任意建開始]', 48, 500, 700)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        # 取得輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYUP:
                waiting = False

def drow_end_init(score):
    SCREEN.fill(BLACK)
    draw_text(SCREEN, '勝利', 128, 500, 200)
    draw_text(SCREEN, f"分數： {score}", 64, 500, 400)
    draw_text(SCREEN, '我很爛，這遊戲沒辦法重新開始，請點擊右上角的叉叉關閉遊戲', 32, 500, 500)
    draw_text(SCREEN, '吳祐感謝你的遊玩(鞠躬)', 32, 500, 600)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

def drow_fail_init(score):
    SCREEN.fill(BLACK)
    draw_text(SCREEN, '失敗 QQ 喔', 128, 500, 200)
    draw_text(SCREEN, f"分數： {score}", 64, 500, 400)
    draw_text(SCREEN, '我很爛，這遊戲沒辦法重新開始，請點擊右上角的叉叉關閉遊戲', 32, 500, 500)
    draw_text(SCREEN, '吳祐感謝你的遊玩(鞠躬)', 32, 500, 600)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True