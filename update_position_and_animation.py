from update_fighter_pos_x import update_x
from update_fighter_pos_y import update_y
from update_anim import update_anim


def update_pos_and_anim(fighter, enemy, f=False):
    update_anim(fighter)
    update_x(fighter, enemy, f)
    update_y(fighter, f)
