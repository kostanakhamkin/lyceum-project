# key = [number of frames,
# frame width,
# list of frames duration,
# loop,
# if char can turn during animation,
# frame with punch and damage ]
sonya_move_animations = {'stand': [7, [45, 48, 47, 46, 46, 46, 50], [1] * 7, [0, 11], True, False],
                           'walk_f': [9, [60, 43, 43, 45, 45, 47, 44, 49, 60], [1] * 9, [0, 8], True, False],
                           'walk_b': [9, [60, 43, 43, 45, 45, 47, 44, 49, 60], [1] * 9, [0, 8], True, False],
                           'jump': [3, [54, 56, 45], [3, 3, 5], [0, 2], False, False],
                           'move_jump': [8, [35, 43, 50, 60, 55, 43, 50, 68], [1] * 8, [1, 7], False, False],
                           'duck': [2, [46, 42], [1] * 4, [2, 2], False, False],
                           'block': [2, [47, 49], [2, 1], [0, 0], False, False],

                           'high_punch': [3, [60, 60, 71], [1, 1, 5], [], False, [[2], 'weak_hit', 30, [4, 0]]],
                           'low_punch': [2, [60, 70], [1, 5], [], False, [[1], 'weak_hit', 30, [4, 0]]],
                           'high_kick': [5, [51, 48, 78, 74, 52], [1, 1, 1, 1, 3, 1], [], False,
                                         [[4], 'weak_hit', 50, [6, 0]]],
                           'low_kick': [5, [51, 48, 78, 83, 64], [1, 1, 1, 1, 3], [], False,
                                        [[4], 'weak_hit', 50, [6, 0]]],
                           'uppercut': [2, [49, 73], [1, 3], [], False,
                                        [[2, 3, 4], 'heavy_hit', 60, [10, -20]]],
                           'sweep_kick': [7, [57, 55, 56, 89, 88, 53, 79], [1] * 7, [], False,
                                          [[3, 4], 'trip', 40, [0, 0]]],
                           'roundhouse': [6, [41, 64, 58, 77, 71, 62], [1] * 6, [], False,
                                          [[2, 3], 'heavy_hit', 70, [10, -20]]],
                           'throw': [6, [66, 84, 61, 62, 53, 78], [1] * 6, [], False,
                                     [[3], 'thrown', 60, [-10, -20]]],
                           'air_kick': [2, [76, 123], [3, 3], [], False, [[1], 'heavy_hit', 40, [7, 0]]],

                           'weak_hit': [3, [46, 47, 58], [1] * 3, [], False, False],
                           'heavy_hit': [7, [55, 84, 84, 54, 69, 87, 104], [2, 2, 5, 2, 2, 2, 2], [], False, False],
                           'trip': [6, [73, 54, 60, 61, 68, 90], [1] * 6, [], False, False],
                           'stand_up': [5, [45, 46, 53, 72, 56], [1] * 5, [], False, False],
                           'thrown': [7, [65, 61, 71, 63, 64, 78, 90], [1, 1, 1, 1, 1, 1, 10], [], False, False],

                           'dead': [7, [50] * 7, [2] * 7, [0, 6], False, False]}

sonya_attack_animations = ['low_punch', 'high_punch', 'low_kick', 'high_kick', 'uppercut', 'sweep_kick', 'roundhouse',
                             'throw', 'air_kick']
