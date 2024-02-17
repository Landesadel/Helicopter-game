from utils import get_rand_cell
import os

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
        self.health = 50

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
        print('🎖️', self.score, end=' | ')
        print('🧡', self.health)

    def game_over(self):
        os.system('clear')
        print('GAME OVER, YOUR SCORE IS: ', self.score)
        exit(0)

    def export_data(self):
        return {
            'score': self.score,
            'health': self.health,
            'x': self.point_x,
            'y': self.point_y,
            'tank': self.tank,
            'tank_capacity': self.tank_capacity
        }
    
    def import_data(self, data):
        self.point_x = data['x'] or 0
        self.point_y = data['y'] or 0
        self.score = data['score'] or 0
        self.health = data['health'] or 50
        self.tank = data['tank'] or 0
        self.tank_capacity = data['tank_capacity'] or 1