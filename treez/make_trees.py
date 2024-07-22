import random
from treez import AsciiCanvas, Coords

class Trunk(AsciiCanvas):
    def __init__(self, *args):
        self.fill('|')

class Crown(AsciiCanvas):
    def __init__(self, width, height):
        half_width = width // 2
        for h in range(height):
            len_crown = min(h + 1, width)
            c_start = half_width - len_crown // 2
            c_end = half_width + len_crown // 2
            self[h, c_start:c_end] = 'x'

class Tree(AsciiCanvas):
    def __init__(self, width, height):
        trunk_width_factor = random.uniform(0.2, 0.4)
        trunk_height_factor = random.uniform(0.1, 0.3)

        width_trunk = max(int(width * trunk_width_factor), 1)
        height_trunk = max(int(height * trunk_height_factor), 1)

        trunk = Trunk(width_trunk, height_trunk)
        trunk_offset = (int((width - width_trunk)/2), height - height_trunk)
        self.add_element(trunk, trunk_offset)

        crown_height = height - height_trunk
        crown_width = width
        crown = Crown(crown_width, crown_height)
        self.add_element(crown)

class Forest(AsciiCanvas):
    def __init__(self, tree, width, height, n_trees, min_h, max_h, method):
        self.tree = tree
        self.min_h = min_h
        self.max_h = max_h
        self.method = method

        coords = Coords(width, height, n_trees, method).coords
        for coord in coords:
            height = random.randint(min_h, max_h)
            element = self.tree(height, height)
            self.add_element(element, coord)

    def add_tree(self):
        height = random.randint(self.min_h, self.max_h)
        coords = Coords(height, height, 1, self.method).coords[0]




