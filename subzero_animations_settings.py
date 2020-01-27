# key = [number of frames,
# frame width,
# list of frames duration,
# loop,
# if char can turn during animation,
# frame with punch and damage ]
subzero_move_animations = {'stand': [12, [51] * 12, [1] * 12, [0, 11], True, False],
                           'walk_f': [9, [52] * 9, [1] * 9, [0, 8], True, False],
                           'walk_b': [9, [52] * 9, [1] * 9, [0, 8], True, False],
                           'jump': [3, [50] * 3, [3, 3, 5], [0, 2], False, False],
                           'move_jump': [8, [49] * 8, [1] * 8, [1, 7], False, False],
                           'duck': [3, [52] * 3, [1] * 5, [2, 2], False, False],
                           'block': [1, [50], [1], [0, 0], False, False],

                           'high_punch': [3, [60, 60, 71], [1, 1, 5], [], False, [[2], 'weak_hit', 30, [4, 0]]],
                           'low_punch': [2, [60, 70], [1, 5], [], False, [[1], 'weak_hit', 30, [4, 0]]],
                           'high_kick': [6, [55, 56, 45, 65, 88, 64], [1, 1, 1, 1, 3, 1], [], False, [[4], 'weak_hit', 50, [6, 0]]],
                           'low_kick': [6, [55, 56, 45, 63, 92, 64], [1, 1, 1, 1, 3, 1], [], False, [[4], 'weak_hit', 50, [6, 0]]],
                           'uppercut': [6, [56, 60, 82, 53, 52, 55], [1, 1, 1, 6, 1, 1], [], False, [[2, 3, 4], 'heavy_hit', 60, [10, -20]]],
                           'sweep_kick': [8, [57, 55, 56, 89, 88, 53, 79, 50], [1] * 8, [], False, [[3, 4], 'trip', 40, [0, 0]]],
                           'roundhouse': [8, [57, 62, 87, 61, 53, 54, 60, 50], [1] * 8, [], False, [[2, 3], 'heavy_hit', 70, [10, -20]]],
                           'throw': [7, [66, 84, 61, 62, 53, 78, 78], [1] * 7, [], False, [[3], 'thrown', 60, [-10, -20]]],
                           'air_kick': [2, [41, 82], [3, 3], [], False, [[1], 'heavy_hit', 40, [7, 0]]],
                           
                           'weak_hit': [3, [56, 59, 60], [2] * 3, [], False, False],
                           'heavy_hit': [6, [79, 82, 63, 53, 79, 100], [2, 2, 5, 2, 2, 2], [], False, False],
                           'trip': [6, [72, 70, 68, 60, 77, 68], [1] * 6, [], False, False],
                           'stand_up': [5, [45, 46, 53, 72, 56], [1] * 5, [], False, False],
                           'thrown': [7, [65, 61, 71, 63, 64, 78, 90], [1, 1, 1, 1, 1, 1, 10], [], False, False],

                           'dead': [7, [49, 54, 50, 49, 56, 52, 52], [2] * 7, [0, 6], False, False]}

subzero_attack_animations = ['low_punch', 'high_punch', 'low_kick', 'high_kick', 'uppercut', 'sweep_kick', 'roundhouse',
                             'throw', 'air_kick']
