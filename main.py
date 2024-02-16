from Map import Map
import time
import os

TECK_SLEEP = 0.06
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_WIDTH, MAP_HEIGHT = 20, 10

test_map = Map(MAP_WIDTH, MAP_HEIGHT)
test_map.generate_forest(3, 10)
test_map.generate_rivers(10)
test_map.generate_rivers(30)
test_map.get_map()

tick = 1

while True:
    os.system("clear")

    test_map.get_map()
    tick += 1
    time.sleep(TECK_SLEEP)

    if (tick % TREE_UPDATE == 0):
        test_map.generate_tree()
        test_map.generate_fir_tree()
    
    if (tick % FIRE_UPDATE == 0):
        test_map.update_fire()