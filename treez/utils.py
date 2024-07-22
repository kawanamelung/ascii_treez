import numpy as np
import time
from scipy.stats import qmc

class AsciiCanvas(np.ndarray):
    def __new__(cls, width, height, *args, **kwargs):
        shape = (height, width)
        obj = np.empty(shape, dtype=object).view(cls)
        obj.fill(' ')
        obj.elements = []
        return obj


    def add_element(self, element, offset=(0, 0)):
        x_start, y_start = offset
        y_end = min(y_start + element.shape[0], self.shape[0])
        x_end = min(x_start + element.shape[1], self.shape[1])

        element_part = element[:y_end - y_start, :x_end - x_start]
        # Create a mask for non-space elements
        e_mask = element_part != ' '

        # Directly apply the mask to update the canvas
        self[y_start:y_end, x_start:x_end][e_mask] = element_part[e_mask]

        self.elements.append((element, offset))

    def __str__(self):
        return '\n'.join(''.join(row) for row in self)

    def flip(self, axis=0):
        if axis == 0:
            self[:] = self[::-1]
        elif axis == 1:
            self[:] = self[:, ::-1]

class AsciiAnimateForest:
    def __init__(self, forest, direction='right'):
        self.set_offset(direction)
        self.forest = forest
        self.elements = forest.elements
        self.shape = forest.shape
        try:
            self.animate()
        except KeyboardInterrupt:
            raise KeyboardInterrupt

    def animate(self):
        offset = self.offset
        elements = self.elements
        while True:
            frame = AsciiCanvas(self.shape[1], self.shape[0])
            for  tree in elements:
                ascii = tree[0]
                coord = tree[1]
                try:
                    frame.add_element(ascii, (coord[0]+offset[0], coord[1]+offset[1]))
                except IndexError:
                    height = np.random.randint(self.forest.min_h, self.forest.max_h)
                    coord = self.get_new_coord()
                    new_tree = self.forest.tree(height, height)
                    frame.add_element(new_tree, coord)

            print(frame)
            time.sleep(0.1)

            elements = frame.elements

    def set_offset(self, direction):
        if direction == 'right':
            self.offset = [1, 0]
        elif direction == 'down':
            self.offset = [0, 1]


    def get_new_coord(self):

        x = np.random.randint(0, self.shape[1])
        y = np.random.randint(0, self.shape[0])
        new_coord = [self.offset[1] * x, self.offset[0] * y]
        print('new coord', new_coord)
        return new_coord

class Coords:
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

