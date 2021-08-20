from maineed.initialize import *


# 碰撞事件
def collision_event(a, b, a_boolean, b_boolean):
    return pygame.sprite.groupcollide(a, b, a_boolean, b_boolean)


# 重生
def reborn_rocks():
    r = Rock()
    MAIN_SHOW.add(r)
    rocks.add(r)
