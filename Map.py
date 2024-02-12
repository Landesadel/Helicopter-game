# 🌲 🌳 🟩 🟦 🚁 🔥 🏥 🏢 🧡 🌩️ 🌧️ 🌥️ 🎖️ 🏆 🧜‍♀️ 🧚 🟫  TODO потом убрать
 
class Map(object):
    CELL_TYPES = '🟩🌲🟦🏥🏢';

    def generate_rivers():
        pass

    def generate_forest():
        pass

    # 0 - поле
    # 1 - дерево
    # 2 - река
    # 3 - госпиталь
    # 4 - апгрейд-шоп
    def get_map(self):
        print('🟫' * (self.width + 2))

        for row in self.cells:
            print('🟫', end='')

            for cell in row:
                if (cell >= 0 and cell < len(self.CELL_TYPES)):
                    print(self.CELL_TYPES[cell], end='')

            print('🟫')

        print('🟫' * (self.width + 2))      

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for i in range(width)] for j in range(height)]

    def is_bounds(self, point_x, point_y):
        if (
            point_x < 0 or point_y < 0 or 
            point_x >= self.height or point_y >= self.width
           ):
            return False
        return True

