from scipy.stats import qmc
import numpy as np
from itertools import repeat, cycle

class AsciiCanvas(np.ndarray):
    def __new__(cls, width, height, *args, **kwargs):
        shape = (height, width)
        obj = np.empty(shape, dtype=object).view(cls)
        obj.fill(' ')
        return obj

    def add_element(self, element, offset=(0, 0)):
        x_start, y_start = offset
        y_end = min(y_start + element.shape[0], self.shape[0])
        x_end = min(x_start + element.shape[1], self.shape[1])

        # Calculate the valid region within the canvas
        canvas = self[y_start:y_end, x_start:x_end]

        # Calculate the valid region within the element
        element_part = element[:y_end - y_start, :x_end - x_start]

        e_mask = element_part != ' '
        canvas[e_mask] = element_part[e_mask]

    def flip(self, axis=0):
        if axis == 0:
            self[:] = self[::-1]
        elif axis == 1:
            self[:] = self[:, ::-1]
    def __str__(self):
        return '\n'.join([''.join(row) for row in self])

class TreeCoords:
    def __init__(self, width, height, n_trees, method='lhc'):
        self.width = width
        self.height = height
        self.n_trees = n_trees
        self.padding = 0

        if method == 'random':
            self.coords = self.random()
        elif method == 'lhc':
            self.coords = self.latin_hyper_cube()
        else:
            raise ValueError('Method not recognized')

    def random(self):
        coords = []
        for _ in range(self.n_trees):
            x = np.random.randint(0, self.width-1)
            y = np.random.randint(0, self.height)
            coords.append((x,y))
        return coords

    def latin_hyper_cube(self):
        sampler = qmc.LatinHypercube(d=2, strength=1)
        samples = sampler.random(n=self.n_trees)
        l_bounds = [self.padding, self.padding]
        u_bounds = [self.width - self.padding, self.height - self.padding]
        return qmc.scale(samples, l_bounds, u_bounds).astype(int)

class Trunk(AsciiCanvas):
    def __init__(self, *args):
        self.fill('|')

class Crown(AsciiCanvas):
    def __init__(self, width, height):
        for h in range(height):
            len_crown = min(h+1, width)
            c_start = int(width/2 - len_crown/2)
            c_end = int(width/2 + len_crown/2)
            self[h, c_start:c_end] = 'x'

class Tree(AsciiCanvas):
    def __init__(self, width, height):
        trunk_width_factor = np.random.uniform(0.2, 0.4)
        trunk_height_factor = np.random.uniform(0.1, 0.3)

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
    def __init__(self, width, height, n_trees, min_h, max_h, **kwargs):
        coords = TreeCoords(width, height, n_trees, **kwargs).coords
        for coord in coords:
            height = np.random.randint(min_h, max_h)
            tree = Tree(height, height)
            self.add_element(tree, coord)

