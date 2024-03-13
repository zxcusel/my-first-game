import pygame
import time
fps = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1228, 717))
pygame.display.set_caption("Nikita the archer")
# IMAGE
stand = pygame.image.load('hero/hero.png').convert_alpha()
leftstand = pygame.image.load('hero/lefthero.png').convert_alpha()
rightDash = [pygame.image.load('hero/dash/dash1.png').convert_alpha(),
             pygame.image.load('hero/dash/dash1.png').convert_alpha(),
             pygame.image.load('hero/dash/dash1.png').convert_alpha(),
             pygame.image.load('hero/dash/dash2.png').convert_alpha(),
             pygame.image.load('hero/dash/dash2.png').convert_alpha(),
             pygame.image.load('hero/dash/dash2.png').convert_alpha(),
             pygame.image.load('hero/dash/dash3.png').convert_alpha(),
             pygame.image.load('hero/dash/dash3.png').convert_alpha(),
             pygame.image.load('hero/dash/dash3.png').convert_alpha(),
             pygame.image.load('hero/dash/dash4.png').convert_alpha(),
             pygame.image.load('hero/dash/dash4.png').convert_alpha(),
             pygame.image.load('hero/dash/dash4.png').convert_alpha(),
             pygame.image.load('hero/dash/dash5.png').convert_alpha(),
             pygame.image.load('hero/dash/dash5.png').convert_alpha(),
             pygame.image.load('hero/dash/dash5.png').convert_alpha(),
             pygame.image.load('hero/dash/dash6.png').convert_alpha(),
             pygame.image.load('hero/dash/dash6.png').convert_alpha(),
             pygame.image.load('hero/dash/dash6.png').convert_alpha(),
             pygame.image.load('hero/dash/dash7.png').convert_alpha(),
             pygame.image.load('hero/dash/dash7.png').convert_alpha(),
             pygame.image.load('hero/dash/dash7.png').convert_alpha(),
             pygame.image.load('hero/dash/dash7.png').convert_alpha(),
             ]
leftDash = [pygame.image.load('hero/dash/leftdash1.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash1.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash1.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash2.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash2.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash2.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash3.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash3.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash3.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash4.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash4.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash4.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash5.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash5.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash5.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash6.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash6.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash6.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash7.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash7.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash7.png').convert_alpha(),
            pygame.image.load('hero/dash/leftdash7.png').convert_alpha(),
            ]
attack = [pygame.image.load('hero/attack/attack1.png').convert_alpha(),
          pygame.image.load('hero/attack/attack1.png').convert_alpha(),
          pygame.image.load('hero/attack/attack1.png').convert_alpha(),
          pygame.image.load('hero/attack/attack1.png').convert_alpha(),
          pygame.image.load('hero/attack/attack2.png').convert_alpha(),
          pygame.image.load('hero/attack/attack2.png').convert_alpha(),
          pygame.image.load('hero/attack/attack2.png').convert_alpha(),
          pygame.image.load('hero/attack/attack2.png').convert_alpha(),
          pygame.image.load('hero/attack/attack3.png').convert_alpha(),
          pygame.image.load('hero/attack/attack3.png').convert_alpha(),
          pygame.image.load('hero/attack/attack3.png').convert_alpha(),
          pygame.image.load('hero/attack/attack3.png').convert_alpha(),
          pygame.image.load('hero/attack/attack4.png').convert_alpha(),
          pygame.image.load('hero/attack/attack4.png').convert_alpha(),
          pygame.image.load('hero/attack/attack4.png').convert_alpha(),
          pygame.image.load('hero/attack/attack4.png').convert_alpha(),
          pygame.image.load('hero/attack/attack4.png').convert_alpha(),
          pygame.image.load('hero/attack/attack5.png').convert_alpha(),
          pygame.image.load('hero/attack/attack5.png').convert_alpha(),
          pygame.image.load('hero/attack/attack5.png').convert_alpha(),
          pygame.image.load('hero/attack/attack5.png').convert_alpha(),
          pygame.image.load('hero/attack/attack6.png').convert_alpha(),
          pygame.image.load('hero/attack/attack6.png').convert_alpha(),
          pygame.image.load('hero/attack/attack6.png').convert_alpha(),
          pygame.image.load('hero/attack/attack6.png').convert_alpha(),
          pygame.image.load('hero/attack/attack6.png').convert_alpha(),
          ]
jump = [
    pygame.image.load('hero/jump/rightjump5.png').convert_alpha(),
    pygame.image.load('hero/jump/jump6.png').convert_alpha(),
]
leftjump = [
    pygame.image.load('hero/jump/leftjump5.png').convert_alpha(),
    pygame.image.load('hero/jump/leftjump6.png').convert_alpha(),
]
walk_right = [
    pygame.image.load('hero/Walk/rightwalk1.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk1.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk1.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk2.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk2.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk2.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk3.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk3.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk3.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk4.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk4.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk4.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk5.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk5.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk5.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk6.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk6.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk6.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk7.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk7.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk7.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk8.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk8.png').convert_alpha(),
    pygame.image.load('hero/Walk/rightwalk8.png').convert_alpha()
]
walk_left = [
    pygame.image.load('hero/Walk/leftwalk1.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk1.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk1.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk2.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk2.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk2.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk3.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk3.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk3.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk4.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk4.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk4.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk5.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk5.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk5.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk6.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk6.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk6.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk7.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk7.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk7.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk8.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk8.png').convert_alpha(),
    pygame.image.load('hero/Walk/leftwalk8.png').convert_alpha()
]
stayNightborne = [pygame.image.load('enemy/хуета/leftnightborne1.png').convert_alpha()]

walkNightborne = [pygame.image.load('enemy/walk/leftwalkborne1.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne1.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne1.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne2.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne2.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne2.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne3.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne3.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne3.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne4.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne4.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne4.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne5.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne5.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne5.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne6.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne6.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne6.png').convert_alpha(),
                  pygame.image.load('enemy/walk/leftwalkborne6.png').convert_alpha(),
                  ]
beast = [pygame.image.load('enemy/monster/demon1.png').convert_alpha()]


thorn = pygame.image.load('platform/thorn.png').convert_alpha()
thorn1 = pygame.image.load('platform/thorn2.png').convert_alpha()
platform = [pygame.image.load('platform/ультра длинный блок.png').convert_alpha(),
            pygame.image.load('platform/блок покоцаный.png').convert_alpha(),
            pygame.image.load('platform/блок.png').convert_alpha(),
            pygame.image.load('platform/длинее длиного блок.png').convert_alpha(),
            pygame.image.load('platform/длиный блок покоцаный.png').convert_alpha(),
            pygame.image.load('platform/еще блок покоцаный.png').convert_alpha(),
            pygame.image.load('platform/еще блок.png').convert_alpha(),
            pygame.image.load('platform/очень покоцаный блок.png').convert_alpha(),
            pygame.image.load('platform/широкий блок покоцаный.png').convert_alpha(),
            ]

HUETA = pygame.image.load('Background/3.png').convert_alpha()

helth_img = pygame.image.load('hp/hp.png').convert_alpha(),
health = 2
# SETTING
nightborne_x = 1400
player_die_count = 0
player_anim_count = 0
player_jump_count = 0
player_attack_count = 0

borne_walk_count = 0
borne_boom_count = 0

beast_attack_count = 0
beast_x = 0



player_speed = 7
player_x = 1
player_y = 557
is_jump = False
jump_count = 8

nightborne_hp = 1

bg_x = 0
platform_x = 0
thorn_x = 1878
thorn_x1 = 0



arrow = pygame.image.load('hero/projectile.png').convert_alpha()
arrows = []
label = pygame.font.Font('fonts/NeedleteethSP_0.otf', 120)
lose_label = label.render('YOU DIED', False, (255, 0, 0))
win_label = label.render('You win!!!',False,(255, 255, 0))
gameplay = True

running = True
while running:
    if gameplay == True:
        background = pygame.image.load('Background/Forest/Reference.png').convert_alpha()
        screen.blit(background, (bg_x, 0))
        screen.blit(background, (bg_x + 1228, 0))
        screen.blit(background, (bg_x + 2456, 0))
        screen.blit(background, (bg_x + 3684, 0))
        screen.blit(background, (bg_x + 4912, 0))
        screen.blit(background, (bg_x + 6140, 0))
        screen.blit(background, (bg_x + 7368, 0))
        screen.blit(background, (bg_x + 8586, 0))

        player_rect = stand.get_rect(topleft=(player_x - 10, player_y))
        if borne_walk_count < len(walkNightborne):
            nightborne_rect = walkNightborne[borne_walk_count].get_rect(topleft=(nightborne_x, 600))
        thorn_rect = thorn.get_rect(topleft=(thorn_x, 640))
        thorn_rect1 = thorn1.get_rect(topleft=(thorn_x1 + 2363, 640))
        platform_rect1 = platform[1].get_rect(topleft=(platform_x + 2671, 525))
        platform_rect1_1 = platform[1].get_rect(topleft=(platform_x + 2936, 525))
        platform_rect2 = platform[2].get_rect(topleft=(platform_x + 2171, 505))
        win_rect = stand.get_rect(topleft=(platform_x + 10000, player_y))


# LEVEL
        screen.blit(platform[0], (platform_x, 653))
        screen.blit(thorn, (thorn_x, 653))
        screen.blit(platform[3], (platform_x + 1979, 653))
        screen.blit(platform[2],(platform_x + 2171, 525))
        screen.blit(thorn1, (thorn_x1 + 2363, 653))
        screen.blit(platform[1], (platform_x + 2671, 525))
        screen.blit(platform[1], (platform_x + 2936, 525))
        screen.blit(platform[0], (platform_x + 3301, 653))

        screen.blit(beast[0], (platform_x + 4600, 397))

# ANIMATION
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and keys[pygame.K_a]:
            screen.blit(leftjump[player_jump_count], (player_x, player_y))
        elif keys[pygame.K_SPACE]:
            screen.blit(jump[player_jump_count], (player_x, player_y))
            if keys[pygame.K_d]:
                if player_x > 500:
                    bg_x -= player_speed
                    platform_x -= player_speed
                    thorn_x1 -= player_speed
                    nightborne_x -= player_speed
                    thorn_x -= player_speed
                    beast_x -= player_speed
        elif keys[pygame.K_a]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        elif keys[pygame.K_d]:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
            if player_x > 500:
                bg_x -= player_speed
                platform_x -= player_speed
                thorn_x1 -= player_speed
                nightborne_x -= player_speed
                thorn_x -= player_speed
                beast_x -= player_speed

        elif keys[pygame.K_f]:
            screen.blit(attack[player_attack_count], (player_x, player_y))
            if player_attack_count == 24:
                arrows.append(arrow.get_rect(topleft=(player_x + 50, player_y + 50)))
        else:
            screen.blit(stand, (player_x, player_y))

        if keys[pygame.K_d] and player_x < 624:
            player_x += player_speed
        elif keys[pygame.K_a] and player_x > 0:
            player_x -= player_speed
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -8:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2

                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 0.5
            else:
                is_jump = False
                jump_count = 8
            if is_jump:
                player_speed = 9
            else:
                player_speed = 7

        if arrows:
            for (i, el) in enumerate(arrows):
                screen.blit(arrow, (el.x, el.y))
                el.x += 35
                if el.x > 1228:
                    arrows.pop(i)
                if el.colliderect(nightborne_rect):
                    walkNightborne.clear()


        if player_attack_count == 24:
            player_attack_count = 0
        else:
            player_attack_count += 1
        if player_anim_count == 23:
            player_anim_count = 0
        else:
            player_anim_count += 1
        if borne_walk_count == 18:
            borne_walk_count = 0
        else:
            borne_walk_count += 1
        if borne_boom_count == 35:
            borne_boom_count = 0
        elif borne_boom_count > -1:
            borne_boom_count += 1
        if beast_attack_count == 40:
            beast_attack_count = 0
        else:
            beast_attack_count += 1

        if player_rect.colliderect(nightborne_rect):
            nightborne_hp -= 1
            if nightborne_hp <= 0:
                screen.fill((0, 0, 0))
                screen.blit(lose_label, (520, 300))
                gameplay = False

#DIE
        if player_rect.colliderect(thorn_rect):
            screen.fill((0, 0, 0))
            screen.blit(lose_label, (520, 300))
            gameplay = False
        elif player_rect.colliderect(thorn_rect1):
            screen.fill((0, 0, 0))
            screen.blit(lose_label, (520, 300))
            gameplay = False
        if player_rect.colliderect(nightborne_rect):
            screen.fill((0, 0, 0))
            screen.blit(lose_label, (520, 300))
            gameplay = False
        elif player_x > nightborne_x - 1000:
            nightborne_x -= 10
            if borne_walk_count < len(walkNightborne):
                screen.blit(walkNightborne[borne_walk_count], (nightborne_x, 545))
        else:
            screen.blit(stayNightborne[0],(nightborne_x, 545))

        if player_rect.colliderect(platform_rect2) and player_y > 440:
            if player_x < player_x -15:
                player_speed = 0
            else:
                player_x -= 15
        elif player_rect.colliderect(platform_rect2) and player_y <= 440:
            jump_count = 8
            if keys[pygame.K_SPACE]:
                is_jump = True
            else:
                is_jump = False
        if not player_rect.colliderect(platform_rect1) and not player_rect.colliderect(platform_rect2) and not player_rect.colliderect(platform_rect1_1):
            if player_y < 557 and is_jump == False:
                player_y += (jump_count ** 2) / 2
            elif player_y > 557:
                player_y = 557


        if player_rect.colliderect(platform_rect1) and player_y > 525:
            if player_x < player_x -15:
                player_speed = 0
            else:
                player_x -= 15
        elif player_rect.colliderect(platform_rect1) and player_y <= 525:
            jump_count = 8
            if keys[pygame.K_SPACE]:
                is_jump = True
            else:
                is_jump = False
        if player_rect.colliderect(platform_rect1_1) and player_y > 525:
            if player_x < player_x -15:
                player_speed = 0
            else:
                player_x -= 15
        elif player_rect.colliderect(platform_rect1_1) and player_y <= 525:
            jump_count = 8
            if keys[pygame.K_SPACE]:
                is_jump = True
            else:
                is_jump = False

        if player_rect.colliderect(win_rect):
            screen.fill((0, 0, 200))
            screen.blit(win_label, (520, 300))
            gameplay = False
        else:
            gameplay = True

        screen.blit(HUETA,(0, 0))
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

fps.tick(60)