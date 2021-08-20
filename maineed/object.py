from maineed.pre_initialize import *
import random


# 角色
class Player(pygame.sprite.Sprite):
    def __init__(self, psi):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.image = set_size_X_Y(player_img, 50, 38)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        # 位置
        self.rect.x = 450
        self.rect.y = 900
        # 參數
        self.psi = psi
        self.speed = 10
        self.helf = 100
        self.shoot_count = 0
        self.shoot_fast = False

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.rect.x += self.speed
        if key_pressed[pygame.K_a]:
            self.rect.x -= self.speed
        if key_pressed[pygame.K_w]:
            self.rect.y -= self.speed
        if key_pressed[pygame.K_s]:
            self.rect.y += self.speed

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HIGH:
            self.rect.bottom = HIGH

    def shoot(self):
        self.shoot_count += 1
        if self.shoot_count >= self.psi:
            shoot_sound.play()
            bullet = Bullet(self.rect.centerx, self.rect.top)
            MAIN_SHOW.add(bullet)
            bullets.add(bullet)
            self.shoot_count = 0


class Power1(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.type = 's1'
        self.image = power_pngs[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # 位置
        self.rect.center = center
        # 參數
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HIGH:
            self.kill()


class Power2(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.type = 's2'
        self.image = power_pngs[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # 位置
        self.rect.center = center
        # 參數
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HIGH:
            self.kill()


# 敵人
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.image_ori = rock_png
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2 - 3
        # 位置
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-2000, -100)
        self.speedy = random.randrange(2, 10)
        self.speedx = random.randrange(-2, 2)
        self.total_dgree = 0
        self.rot_degree = random.randrange(-3, 3)

    def rotate(self):
        self.total_dgree += self.rot_degree
        self.total_dgree = self.total_dgree % 360
        self.image = pygame.transform.rotate(self.image_ori, self.total_dgree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HIGH:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-2, 2)


class PirateShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.image = explship_pngs[0]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        # 位置
        self.rect.x = random.randrange(200, 800)
        self.rect.y = random.randrange(-500, -100)
        # 參數
        self.shoot_count = 0
        self.helf = 100
        self.speedy = 1
        self.speedx = 0

    def update(self):
        # 移動
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HIGH:
            self.rect.x = random.randrange(200, 800)
            self.rect.y = random.randrange(-500, -100)
            self.speedy = 1
            self.speedx = 0
        # 射擊
        self.shoot_count += 1
        if self.shoot_count == pirate_ship_psi:
            n1_sound.play()
            enemybullet = EnemyBullet(self.rect.centerx, self.rect.top)
            MAIN_SHOW.add(enemybullet)
            enemybullets.add(enemybullet)
            self.shoot_count = 0


class Boss(pygame.sprite.Sprite):
    def __init__(self, psi):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.image = boss_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2
        # 位置
        self.rect.x = 100
        self.rect.y = -1000
        # 參數
        self.psi = psi
        self.sound_count = 100
        self.shoot_count = 0
        self.shoot_cool = 0
        self.pmove_count = 0
        self.nmove_count = -600
        self.helf = 300
        self.speedy = 1
        self.speedx = 0
        self.openfire = False

    def update(self):
        # 移動
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # 動作
        if self.rect.top == 0:
            self.speedy = 0
            self.openfire = True
        # 射擊
        if self.openfire is True:
            self.shoot_count += 1
            self.shoot_cool += 1
            if self.shoot_cool < 300:
                if self.shoot_count >= self.psi:
                    self.sound_count += 1
                    if self.sound_count >= 100:
                        b1_sound.play()
                        self.sound_count = 0
                    enemybullet = EnemyBullet(self.rect.centerx - 125, self.rect.top)
                    MAIN_SHOW.add(enemybullet)
                    enemybullets.add(enemybullet)
                    enemybullet = EnemyBullet(self.rect.centerx + 125, self.rect.top)
                    MAIN_SHOW.add(enemybullet)
                    enemybullets.add(enemybullet)
                    enemybullet2 = EnemyBullet2(self.rect.centerx, self.rect.top)
                    MAIN_SHOW.add(enemybullet2)
                    enemybullets2.add(enemybullet2)
                    self.shoot_count = 0
            if self.shoot_cool > 600:
                self.shoot_cool = 0

    def move(self):
        self.pmove_count += 1
        self.nmove_count += 1
        if self.pmove_count == 1200:
            self.speedx = 1
            self.pmove_count = 0
        if self.nmove_count == 1200:
            self.speedx = -1
            self.nmove_count = 0


# 子彈
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.image = bullet_png
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2 + 1
        # 位置
        self.rect.centerx = x
        self.rect.bottom = y
        # 參數
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.image = enebullet_png
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2 + 1
        # 位置
        self.rect.centerx = x
        self.rect.bottom = y + 200
        # 參數
        self.speed = 10

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HIGH:
            self.kill()


class EnemyBullet2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.image = bossbullet_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2
        # 位置
        self.rect.centerx = x
        self.rect.bottom = y + 250
        # 參數
        self.xspeed = random.randrange(-15, 15)
        self.yspeed = random.randrange(-15, 15)

    def update(self):
        if self.xspeed == 0:
            self.xspeed = 1
        if self.yspeed == 0:
            self.yspeed = 1
        self.rect.y += self.yspeed
        self.rect.x += self.xspeed

        if self.rect.top > HIGH:
            self.kill()


class EnemyBullet2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.image = bossbullet_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2
        # 位置
        self.rect.centerx = x
        self.rect.bottom = y + 250
        # 參數
        self.xspeed = random.randrange(-15, 15)
        self.yspeed = random.randrange(-15, 15)

    def update(self):
        if self.xspeed == 0:
            self.xspeed = 1
        if self.yspeed == 0:
            self.yspeed = 1
        self.rect.y += self.yspeed
        self.rect.x += self.xspeed

        if self.rect.top > HIGH:
            self.kill()


# 特效
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.size = size
        self.image = expl_anim[self.size][0]
        self.rect = self.image.get_rect()
        # 位置
        self.rect.center = center
        # 參數
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(expl_anim[self.size]):
                self.kill()
            else:
                self.image = expl_anim[self.size][self.frame]
                conter = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = conter


class Explosion2(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.size = size
        self.image = expl_anim[self.size][0]
        self.rect = self.image.get_rect()
        # 位置
        self.rect.x = x + 135 + random.randrange(-80, 80)
        self.rect.y = y + 135 + random.randrange(-80, 80)
        # 參數
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(expl_anim[self.size]):
                self.kill()
            else:
                self.image = expl_anim[self.size][self.frame]
                conter = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = conter


class Explosion3(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.size = size
        self.image = expl_anim[self.size][0]
        self.rect = self.image.get_rect()
        # 位置
        self.rect.x = x + 50 + random.randrange(-80, 80)
        self.rect.y = y + 50 + random.randrange(-80, 80)
        # 參數
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(expl_anim[self.size]):
                self.kill()
            else:
                self.image = expl_anim[self.size][self.frame]
                conter = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = conter


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.width = random.randrange(2, 10)
        self.high = self.width + 5
        self.image = pygame.Surface((self.width, self.high))
        self.image.fill(WHITE)
        # 位置
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.width)
        self.rect.y = random.randrange(-100, -40)
        # 參數
        self.speedy = random.randrange(10, 20)
        self.speedx = random.randrange(-1, 1)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HIGH:
            self.rect.x = random.randrange(0, WIDTH - self.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(10, 20)
            self.speedx = random.randrange(-1, 1)


class Screen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 顯示
        self.image = screen_img
        self.rect = self.image.get_rect()
        # 位置
        self.rect.x = 0
        self.rect.y = -10000
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HIGH:
            self.rect.x = 0
            self.rect.y = -10000
            self.speedy = 5
