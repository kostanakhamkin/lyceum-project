from apply_damage import apply_damage


def collision(sprite1, sprite2):
    if type(sprite1).__name__ == 'Character' and sprite1.damage and not sprite1.hit:
        apply_damage(sprite2, sprite1.curent_animation_settings[5])
        sprite1.hit = True
    if type(sprite2).__name__ == 'Character' and sprite2.damage and not sprite2.hit:
        apply_damage(sprite1, sprite2.curent_animation_settings[5])
        sprite2.hit = True