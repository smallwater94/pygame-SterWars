
from maineed.event import *

print(running)
print(ps_count)
print(psi)
show_init = True
end_init = False
fail_init = False
timer = False
timer2 = 0
play_sound = True
byby = False
gogo = False
gogoc = 0
gogob = 1
while running:
    if show_init:
        background_sound.play()
        byby = drow_init()
        show_init = False
        background_sound.fadeout(10000)

    if end_init:
        byby = drow_end_init(score)
        background_sound2.fadeout(3000)

    if fail_init:
        byby = drow_fail_init(score)
        background_sound2.fadeout(3000)

    clock.tick(FPS)  # 遊戲FPS
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if byby:
        running = False

    # 更新遊戲
    MAIN_SHOW.update()
    player.shoot()
    boss.move()

    # 石頭子彈撞擊
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True, pygame.sprite.collide_circle)
    for hit in hits:
        # 音效
        random.choice(expl_sounds).play()
        # 特效
        expl = Explosion(hit.rect.center, 'md')
        MAIN_SHOW.add(expl)
        # 得分
        score += 100
        # 重生
        reborn_rocks()
    # 石頭玩家撞擊
    hits = pygame.sprite.groupcollide(rocks, players, True, False, pygame.sprite.collide_circle)
    for hit in hits:
        # 音效
        random.choice(damage_sounds).play()
        # 特效
        expl = Explosion(hit.rect.center, 'sm')
        MAIN_SHOW.add(expl)
        # 重生
        reborn_rocks()
        # 傷害
        player.helf -= 5
        # 附加事件
        if player.helf <= 0:
            background_sound2.fadeout(1000)
            fail_init = True
    # 子彈玩家撞擊
    hits = pygame.sprite.groupcollide(enemybullets, players, True, False, pygame.sprite.collide_circle)
    for hit in hits:
        # 音效
        random.choice(damage_sounds).play()
        # 特效
        expl = Explosion(hit.rect.center, 'sm')
        MAIN_SHOW.add(expl)
        # 傷害
        player.helf -= 5
        # 附加事件
        if player.helf <= 0:
            background_sound2.fadeout(1000)
            fail_init = True
    hits = pygame.sprite.groupcollide(enemybullets2, players, True, False, pygame.sprite.collide_circle)
    for hit in hits:
        # 音效
        random.choice(damage_sounds).play()
        # 特效
        expl = Explosion(hit.rect.center, 'sm')
        MAIN_SHOW.add(expl)
        # 傷害
        player.helf -= 10
        # 附加事件
        if player.helf <= 0:
            fail_init = True
    # 海盜船子彈撞擊
    hits = collision_event(pirate_ships, bullets, False, True)
    for hit in hits:
        # 音效
        random.choice(des_sounds).play()
        # 特效
        pirate_ship.image = explship_pngs[ps_count]
        expl = Explosion(hit.rect.center, 'sm')
        MAIN_SHOW.add(expl)
        # 參數

        ps_count += 1
        pirate_ship.helf -= 30

        if pirate_ship.helf <= 0:
            expl = Explosion(hit.rect.center, 'slg')
            MAIN_SHOW.add(expl)
            destruction_song.play()
            score += 1000
            pirate_ship.helf = 100
            pirate_ship.rect.x = random.randrange(200, 800)
            pirate_ship.rect.y = random.randrange(-1000, -200)
            ps_count = 0
            pirate_ship.image = explship_pngs[ps_count]
            x = random.randrange(0, 2)
            if x == 0:
                poww = Power1(hit.rect.center)
                MAIN_SHOW.add(poww)
                powers1.add(poww)
            if x == 1:
                poww = Power2(hit.rect.center)
                MAIN_SHOW.add(poww)
                powers2.add(poww)

    # 魔王子彈撞擊
    hits = pygame.sprite.groupcollide(bosss, bullets, False, True, pygame.sprite.collide_circle)
    for hit in hits:
        # 音效
        des_sound_b.play()
        # 特效
        expl = Explosion2(hit.rect.x, hit.rect.y, 'sm')
        MAIN_SHOW.add(expl)
        # 參數
        boss.helf -= 1
        if boss.helf == 270:
            boss.psi = 5
            des_sound_c.play()
            expl = Explosion(hit.rect.center, 'lg')
            MAIN_SHOW.add(expl)
            destruction_song.play()
            boss.image = boss_img1
            boss.image.set_colorkey(WHITE)

        if boss.helf == 170:
            boss.psi = 3
            des_sound_c.play()
            expl = Explosion(hit.rect.center, 'lg')
            MAIN_SHOW.add(expl)
            destruction_song.play()
            boss.image = boss_img2
            boss.image.set_colorkey(WHITE)

        if boss.helf == 80:
            boss.psi = 1
            des_sound_c.play()
            expl = Explosion(hit.rect.center, 'lg')
            MAIN_SHOW.add(expl)
            destruction_song.play()
            boss.image = boss_img3
            boss.image.set_colorkey(WHITE)

        if boss.helf <= 0:
            boss.psi = 10000
            gogo = True

    if gogo is True:
        gogob += 1
        gogoc += 1
    if gogob % 60 == 0:
        des_sound_c.play()
        expl = Explosion3(boss.rect.x - 50, boss.rect.y - 50, 'lg')
        MAIN_SHOW.add(expl)
        destruction_song.play()
    if gogoc >= 600:
        expl = Explosion(boss.rect.center, 'blg')
        MAIN_SHOW.add(expl)
    if gogoc >= 800:
        score += 10000
        end_init = True
    # 吃寶物1
    hits = collision_event(powers1, players, True, False)
    for hit in hits:
        s1_sound.play()
        player.helf += 50
        if player.helf > 100:
            player.helf = 100
    # 吃寶物2
    hits = collision_event(powers2, players, True, False)
    for hit in hits:
        s2_sound.play()
        player.shoot_fast = True
        player.psi = 10
    if timer == 800:
        player.psi = 20
        timer = 0
        player.shoot_fast = False
    # 計時
    if player.shoot_fast is True:
        timer += 1
    if timer2 < 700:
        timer2 += 1
    if timer2 > 600 and play_sound is True:
        background_sound2.play()
        play_sound = False

    # 畫面顯示
    SCREEN.fill(BLACK)
    MAIN_SHOW.draw(SCREEN)
    draw_text(SCREEN, f"Score: {score}", 26, 75, 900)
    draw_health(SCREEN, player.helf, 5, 950)
    draw_health(SCREEN, boss.helf, 175, 0)
    pygame.display.update()

# 遊戲結束
pygame.quit()
