from Map import Map
from Helicopter import Helicopter
from pynput import keyboard
from pynput import keyboard
import time
import os

TECK_SLEEP = 0.06
TREE_UPDATE = 50
CLOUD_UPDATE = 500
CLOUD_MOVE = 50
FIRE_UPDATE = 75
MAP_WIDTH, MAP_HEIGHT = 20, 10
MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

test_map = Map(MAP_WIDTH, MAP_HEIGHT)

helico = Helicopter(MAP_WIDTH, MAP_HEIGHT)

def action_key(key):
    global helico

    key = key.char

    # проверка на релевантность клавиши
    if (key in MOVES.keys()):
        point_x, point_y = MOVES[key][0], MOVES[key][1]
        helico.move(point_x, point_y)

listener = keyboard.Listener(
    on_press=None,
    on_release=action_key)
listener.start()

tick = 1

while True:
    os.system("clear")
    test_map.process_objest(helico)
    helico.get_info()
    test_map.get_map(helico)
    tick += 1
    time.sleep(TECK_SLEEP)

    if (tick % TREE_UPDATE == 0):
        test_map.generate_tree()
        test_map.generate_fir_tree()
    
    if (tick % FIRE_UPDATE == 0):
        test_map.update_fire(helico)


    if (tick % CLOUD_MOVE == 0):
        test_map.move_clouds(7, 10)