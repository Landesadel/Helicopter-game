from utils import get_rand_bool
from utils import get_rand_cell
from utils import extension_cell

# 🌲 🌳 🟩 🟦 🚁 🔥 🏥 🏢 🧡 🌩️ 🌧️ 🌥️ 🎖️ 🏆 🧜‍♀️ 🧚 🟫 💧 TODO потом убрать
 
class Map(object):
    CELL_TYPES = '🟩🌲🟦🏥🏢🌳🔥'
    TREE_BONUS = 10
    UPGRADE_COST = 300

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for i in range(width)] for j in range(height)]
        self.generate_forest(3, 10)
        self.generate_rivers(10)
        self.generate_rivers(30)
        self.generate_shop()

    def is_bounds(self, point_x, point_y):
        if (
            point_x < 0 or point_y < 0 or 
            point_x >= self.height or point_y >= self.width
        ):
            return False
        return True
    
    # 0 - поле
    # 1 - елка
    # 2 - река
    # 3 - госпиталь
    # 4 - апгрейд-шоп
    # 5 - дерево
    # 6 - огонь
    def get_map(self, object):
        print('🟫' * (self.width + 2))

        for x in range(self.height):
            print('🟫', end='')

            for y in range(self.width):
                cell = self.cells[x][y]

                if (object.point_x == x and object.point_y == y):
                    print('🚁', end='')

                elif (cell >= 0 and cell < len(self.CELL_TYPES)):
                    print(self.CELL_TYPES[cell], end='')

            print('🟫')

        print('🟫' * (self.width + 2))

    def generate_shop(self):
        cell = get_rand_cell(self.width, self.height)
        point_x, point_y = cell[0], cell[1]

        self.cells[point_x][point_y] = 4

    def generate_rivers(self, length):
        river = get_rand_cell(self.width, self.height)
        point_x, point_y = river[0], river[1]

        self.cells[point_x][point_y] = 2

        while length > 0:
            next_cell = extension_cell(point_x, point_y)
            next_x, next_y = next_cell[0], next_cell[1]

            if (self.is_bounds(next_x, next_y)):
                self.cells[next_x][next_y] = 2 
                point_x, point_y = next_x, next_y

                length -= 1


    def generate_forest(self, chance, range_value):
        for i in range(self.height):
            for j in range(self.width):
                if get_rand_bool(chance, range_value):
                    self.cells[i][j] = 1

    def generate_tree(self):
        cell = get_rand_cell(self.width, self.height)

        point_x, point_y = cell[0], cell[1]

        if (self.is_bounds(point_x, point_y) and self.cells[point_x][point_y] == 0):
            self.cells[point_x][point_y] = 5

    def generate_fir_tree(self):
        cell = get_rand_cell(self.width, self.height)
        point_x, point_y = cell[0], cell[1]

        if (self.is_bounds(point_x, point_y) and self.cells[point_x][point_y] == 0):
            self.cells[point_x][point_y] = 1

    def generate_fire(self):
        cell = get_rand_cell(self.width, self.height)
        point_x, point_y = cell[0], cell[1]

        if (self.cells[point_x][point_y] == 1 or self.cells[point_x][point_y] == 5):
            self.cells[point_x][point_y] = 6

    def update_fire(self, object):
        for x in range(self.height):
            for y in range(self.width):
                cell = self.cells[x][y]

                if cell == 6:
                    self.cells[x][y] = 0
                    if object.score > 0:
                        object.score -= 1
        for i in range(7):
            self.generate_fire()     

    def process_objest(self, object):
        object_coordinate = self.cells[object.point_x][object.point_y]
        if (object_coordinate == 2):
            while object.tank_capacity > object.tank:
                object.tank += 1
        
        if (object_coordinate == 6 and object.tank > 0):
            object.tank -= 1
            object.score += self.TREE_BONUS

            self.cells[object.point_x][object.point_y] = 1

        if (object_coordinate == 4 and object.score >= self.UPGRADE_COST):
            object.tank_capacity += 1
            object.score -= self.UPGRADE_COST
