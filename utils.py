from random import randint as rand

def get_rand_bool(chance,range_value):
    number = rand(0, range_value)

    return (number <= chance)

def get_rand_cell(width, height):
    width = rand(0, width - 1)
    height = rand(0, height - 1)

    return (height, width)

def extension_cell(point_x, point_y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    coordinate = rand(0, 3)

    coordinate_x, coordinate_y = moves[coordinate][0], moves[coordinate][1]

    return (point_x + coordinate_x, point_y + coordinate_y)
