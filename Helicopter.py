from utils import get_rand_cell

class Helicopter(object):
    def __init__(self, width, height):
        start_position = get_rand_cell(width, height)

        self.point_x = start_position[0]
        self.point_y = start_position[1]
        self.width = width
        self.height = height
        self.tank = 0
        self.tank_capacity = 1
        self.score = 0

    def move(self, point_x, point_y):
        new_point_x = point_x + self.point_x
        new_point_y = point_y + self.point_y

        if (
            new_point_x >= 0 and new_point_y >= 0 and
            new_point_x < self.height and new_point_y < self.width
        ):
            self.point_x, self.point_y = new_point_x, new_point_y

    def get_info(self):
        print('💧 ', self.tank, '/', self.tank_capacity, sep='', end=' | ')
        print('🎖️', self.score)