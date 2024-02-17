from Map import Map
from Helicopter import Helicopter
from pynput import keyboard
from pynput import keyboard
import time
import os
import json

TECK_SLEEP = 0.06
TREE_UPDATE = 50
CLOUD_UPDATE = 500
CLOUD_MOVE = 50
FIRE_UPDATE = 75
MAP_WIDTH, MAP_HEIGHT = 20, 10
MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

test_map = Map(MAP_WIDTH, MAP_HEIGHT)
helico = Helicopter(MAP_WIDTH, MAP_HEIGHT)
tick = 1

def action_key(key):
    global helico, map

    key = key.char

    # обработка движения вертолета
    if (key in MOVES.keys()):
        point_x, point_y = MOVES[key][0], MOVES[key][1]
        helico.move(point_x, point_y)
    # сохранение игры
    elif key == 'f':
        data = {'helicopter': helico.export_data(), 'map': test_map.export_data()}

        with open('level.json', 'w') as file:
            json.dump(data, file)
    # загрузка игры
    elif key == 'x':
        with open('level.json', 'r') as file:
            data = json.load(file)
            helico.import_data(data['helicopter'])
            Map.import_data(data['map'])
    

listener = keyboard.Listener(
    on_press=None,
    on_release=action_key)
listener.start()

while True:
    os.system("clear")
    test_map.process_objest(helico)
    helico.get_info()
    test_map.get_map(helico)
    test_map.get_cost_info()
    tick += 1
    time.sleep(TECK_SLEEP)

    if (tick % TREE_UPDATE == 0):
        test_map.generate_tree()
        test_map.generate_fir_tree()
    
    if (tick % FIRE_UPDATE == 0):
        test_map.update_fire(helico)


    if (tick % CLOUD_MOVE == 0):
        test_map.move_clouds(7, 10)