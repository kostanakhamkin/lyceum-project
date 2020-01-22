def update_anim(fighter):
    if fighter.getting_damage:
        return

    elif fighter.attack:
        if fighter.attack == 'high_punch' and fighter.cur_anim != 'high_punch' and fighter.on_ground:
            fighter.set_anim('high_punch')

    else:
        if fighter.on_ground and fighter.ducked and fighter.cur_anim != 'duck':
            fighter.set_anim('duck')

        elif fighter.on_ground and not fighter.ducked and fighter.cur_anim == 'duck' and fighter.cur_frame == 2:
            fighter.cur_frame = 3

        elif fighter.on_ground and fighter.block and fighter.cur_anim != 'block':
            fighter.set_anim('block')

        elif fighter.vector[0] != 0 and fighter.cur_anim != 'walk_f' and fighter.on_ground and\
                (fighter.vector[0] > 0 and fighter.side == 'left' or fighter.vector[0] < 0 and fighter.side == 'right')\
                and not fighter.block and not fighter.ducked:
            fighter.set_anim('walk_f')

        elif fighter.vector[0] != 0 and fighter.cur_anim != 'walk_b' and fighter.on_ground and\
                (fighter.vector[0] < 0 and fighter.side == 'left' or fighter.vector[0] > 0 and fighter.side == 'right')\
                and not fighter.block and not fighter.ducked:
            fighter.set_anim('walk_b')

        elif fighter.vector[
            0] == 0 and fighter.cur_anim != 'stand' and fighter.cur_anim != 'duck' and fighter.on_ground\
                and not fighter.block:
            fighter.set_anim('stand')

        elif fighter.vector[
            0] == 0 and fighter.cur_anim != 'jump' and not fighter.on_ground\
                and not fighter.block and not fighter.ducked:
            fighter.set_anim('jump')

        elif fighter.vector[0] != 0 and fighter.cur_anim != 'move_jump' and not fighter.on_ground\
                and not fighter.block and not fighter.ducked:
            fighter.set_anim('move_jump')