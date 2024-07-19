from scipy.stats import qmc
import numpy as np

class AsciiCanvas(np.ndarray):
    def __new__(cls, width: int, height: int, *args, **kwargs):
        shape = (height, width)
        obj = np.empty(shape, dtype=object).view(cls)
        obj.fill(' ')
        return obj

    def add_element(self, element: np.ndarray, offset: tuple[int, int] = (0, 0)):

        max_h = min(offset[0] + element.shape[0], self.shape[0])
        max_w = min(offset[1] + element.shape[1], self.shape[1])

        rows = max_h - offset[0]
        cols = max_w - offset[1]

        # print('Canvas:', self.shape)
        # print('Element:', element.shape)
        # print('Offset:', offset)
        # Create slices for the canvas and element
        canvas_slice = self[offset[0]:max_h, offset[1]:max_w]
        element_slice = element[:rows, :cols]

        msg = f'Element does not fit in canvas. Canvas shape: {canvas_slice.shape}, Element shape: {element_slice.shape}'
        assert canvas_slice.shape == element_slice.shape, msg
        # Create a boolean mask of where the element slice is not empty
        mask = element_slice != ''

        # Apply the mask to update the canvas slice
        canvas_slice[mask] = element_slice[mask]

    def __str__(self):
        return '\n'.join([''.join(row) for row in self])

class TreeCoords:
    def __init__(self, width: int, height: int, n_trees: int, method: str = 'lhc'):
        self.height = height
        self.width = width
        self.n_trees = n_trees
        self.padding = 0

        if method == 'random':
            self.coords = self.random()
        if method == 'lhc':
            self.coords = self.latin_hyper_cube()

    def random(self) -> list:
        coords = []
        for _ in range(self.n_trees):
            x = np.random.randint(0, self.height)
            y = np.random.randint(0, self.width)
            coords.append((x,y))
        return coords

    def latin_hyper_cube(self) -> np.ndarray:
        sampler = qmc.LatinHypercube(d=2, strength=1)
        samples = sampler.random(n=self.n_trees)
        l_bounds = [self.padding, self.padding]
        u_bounds = [self.height - self.padding, self.width - self.padding]
        return qmc.scale(samples, l_bounds, u_bounds).astype(int)

class Trunk(AsciiCanvas):
    def __init__(self, *args):
        self.fill('|')

class Crown(AsciiCanvas):
    def __init__(self, width: int, height : int):
        for h in range(height):
            len_crown = min(h+1, width)
            c_start = int(width/2 - len_crown/2)
            c_end = int(width/2 + len_crown/2)
            self[h, c_start:c_end] = 'x'

class Tree(AsciiCanvas):
    def __init__(self, width: int, height: int):


        scale_trunk_width = np.random.uniform(0.2, 0.4)
        scale_trunk_height = np.random.uniform(0.1, 0.3)

        width_trunk = max(int(width * scale_trunk_width), 1)
        height_trunk = max(int(height * scale_trunk_height), 1)

        trunk_offset = (height - height_trunk, int((width - width_trunk)/2))
        self.add_element(Trunk(width_trunk, height_trunk), trunk_offset)

        crown_height = height - height_trunk
        crown_width = width
        self.add_element(Crown(crown_width, crown_height))


class Forest(AsciiCanvas):
    def __init__(self, width: int, height: int, n_trees: int, min_h: int,
                 max_h: int, **kwargs):
        coords = TreeCoords(width, height, n_trees, **kwargs).coords
        for coord in coords:
            height = np.random.randint(min_h, max_h)
            tree = Tree(height, height)
            self.add_element(tree, coord)
            # break

        # print(canvas)

# class AsciiTree(np.ndarray):
#
#     canvas = AsciiCanvas(*inps.win_size)
#     coords = TreeCoords(inps.win_size, inps.n_trees, inps.method).coords
#     for coord in coords:
#         height = np.random.randint(inps.min, inps.max)
#         tree = AsciiTree(height, height)
#         canvas.add_element(tree, coord)
#         break
