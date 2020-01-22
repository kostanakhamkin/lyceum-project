import pygame
from update_anim import update_anim
from change_fighter_position import change_position
from turn_frame import turn_frame


def update_img(char, side, f=False):
    char.frame_time -= 1
    if char.frame_time == 0:

        if char.curent_animation_settings[3]:
            if char.cur_frame == char.curent_animation_settings[3][1]:
                char.cur_frame = char.curent_animation_settings[3][0] - 1

        if char.cur_frame == len(char.curent_animation_settings[2]) - 1:
            char.cur_anim = ''
            char.attack = False
            char.getting_damage = False
            char.hit = False
            char.vector = [0, 0]
            char.can_turn = True
            turn_frame(char, side)
            update_anim(char)

        else:
            char.cur_frame += 1

        char.frame_time = char.curent_animation_settings[2][char.cur_frame]
    char.image = char.frames[char.cur_frame]

    if char.side == 'right':
        if char.cur_anim == 'high_punch':
            print(char.pos_x, char)
        t = char.pos_x + char.rect.width
        char.rect = char.image.get_rect()
        char.pos_x = t - char.rect.width
        change_position(char)
        if char.cur_anim == 'high_punch':
            print(char.pos_x)
            print('------------------')
    else:
        char.rect = char.image.get_rect()

    char.mask = pygame.mask.from_surface(char.image)
    char.damage = 0
    if char.curent_animation_settings[5]:
        if char.cur_frame == char.curent_animation_settings[5][0]:
            char.damage = char.curent_animation_settings[5][2]

    turn_frame(char, side)