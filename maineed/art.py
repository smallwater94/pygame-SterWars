from maineed.utils import *

# 載入圖片
player_img = add_img("img", "player.png")
player_ico = pygame.transform.scale(player_img,(25, 19))
player_ico.set_colorkey(BLACK)
pygame.display.set_icon(player_ico)
rock_png = add_img("img", "rock.png")
bullet_png = add_img("img", "bullet.png")
enebullet_png = add_img("img", "enebullet.png")
screen_img = add_img("img", "d.png")
# 爆炸圖片
expl_anim = {'blg': [],'lg': [],'slg': [], 'md': [], 'sm': []}
for i in range(9):
    expl_png = pygame.image.load(os.path.join("img", f"expl{i}.png")).convert()
    expl_png.set_colorkey(BLACK)
    expl_anim['blg'].append(set_size(expl_png, 400))
    expl_anim['lg'].append(set_size(expl_png, 275))
    expl_anim['slg'].append(set_size(expl_png, 175))
    expl_anim['md'].append(set_size(expl_png, 75))
    expl_anim['sm'].append(set_size(expl_png, 25))
# 海盜船圖片
explship_pngs = []
for i in range(5):
    explship_png = pygame.image.load(os.path.join("img", f"eneship{i}.png")).convert()
    explship_png.set_colorkey(WHITE)
    explship_pngs.append(pygame.transform.scale(explship_png, (80, 200)))
# 魔王圖片
boss_img = add_img("img", "boss0.png")
boss_img1 = add_img("img", "boss1.png")
boss_img2 = add_img("img", "boss2.png")
boss_img3 = add_img("img", "boss3.png")
bossbullet_img = add_img("img", "bossbullet.png")

# 寶物圖片
power_pngs = {}
power_pngs['s1'] = add_img("img", "shield.png")
power_pngs['s2'] = add_img("img", "gun.png")

# 加入音效
shoot_sound = add_sound("sound", "shoot.wav")
shoot_sound.set_volume(0.1)
# 爆炸音效
expl_sound0 = add_sound("sound", "expl0.wav")
expl_sound0.set_volume(0.1)
expl_sound1 = add_sound("sound", "expl1.wav")
expl_sound1.set_volume(0.1)
expl_sounds = [expl_sound0, expl_sound1]
# 飛船受傷音效
damage_sounds = []
for i in range(5):
    filename = f"damage{i}.wav"
    sound = add_sound("sound", filename)
    sound.set_volume(0.2)
    damage_sounds.append(sound)
# 飛船受傷音效
des_sound0 = add_sound("sound", "sword_attack0.wav")
des_sound0.set_volume(0.2)
des_sound1 = add_sound("sound", "sword_attack1.wav")
des_sound1.set_volume(0.2)
des_sounds = [des_sound0, des_sound1]
# boss 受傷
des_sound_b = add_sound("sound", "bomb.wav")
des_sound_b.set_volume(0.05)
des_sound_c = add_sound("sound", "explosion2.wav")
des_sound_c.set_volume(0.2)
# 敵人攻擊聲
n1_sound = add_sound("sound", "laser2.wav")
n1_sound.set_volume(0.1)
b1_sound = add_sound("sound", "full_laser.wav")
b1_sound.set_volume(0.05)
# 吃寶聲
s1_sound = add_sound("sound", "magic2.wav")
s1_sound.set_volume(0.1)
s2_sound = add_sound("sound", "magic3.wav")
s2_sound.set_volume(0.1)
# 飛船爆炸音效
destruction_song = add_sound("sound", "destruction1.wav")
destruction_song.set_volume(0.2)
# 背景音樂
background_sound = add_sound("sound", "background.wav")
background_sound.set_volume(0.4)
background_sound2 = add_sound("sound", "yt1scom.wav")
background_sound2.set_volume(0.4)