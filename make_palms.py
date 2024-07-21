from treez import AsciiCanvas
class PalmTrunk(AsciiCanvas):
    def __init__(self, width, height, direction, x_pad):
        chars = [('(', ')'), ('|', '|'),('(', ')')]
        self.fill('.')

        if direction == 'left':
            w_offset = [x_pad]*len(chars)
            mod = 0
            for h in range(height-1):
                if h % 2 != 0:
                    w_offset.append(w_offset[-1]+mod)
                    chars.append(('(', ')'))
                else:
                    if np.random.uniform() < 0.4:
                        w_offset.append(w_offset[-1])
                        chars.append(('|', '|'))
                        mod = 0
                    else:
                        w_offset.append(w_offset[-1]+1)
                        chars.append(('\\', '\\'))
                        mod = 1
        elif direction == 'right':
            w_offset = [width-x_pad-1]*len(chars)
            mod = 0
            for h in range(height-1):
                if h % 2 != 0:
                    w_offset.append(w_offset[-1]+mod)
                    chars.append(('(', ')'))
                else:
                    if np.random.uniform() < 0.4:
                        w_offset.append(w_offset[-1])
                        chars.append(('|', '|'))
                        mod = 0
                    else:
                        w_offset.append(w_offset[-1]-1)
                        chars.append(('/', '/'))
                        mod = -1
        for h, char, w in zip(range(height), chars, w_offset):
            self[h, w] = char[0]
            self[h, w+1] = char[1]

class PalmCrown(AsciiCanvas):
    def __init__(self,  width, height, lower_leaves=3):
        center = int(width/2)-1
        height-=1

        self[height-lower_leaves, center:center+2] = ['\\', '/']

        # randomly add coconuts
        # first row
        if np.random.uniform() < 0.5:
            self[height-lower_leaves, center+2] = '@'
            if np.random.uniform() < 0.2:
                self[height-lower_leaves+1, center+2] = '@'
        if np.random.uniform() < 0.5:
            self[height-lower_leaves, center-1] = '@'
            if np.random.uniform() < 0.2:
                self[height-lower_leaves+1, center-1] = '@'

        if np.random.uniform() < 0.5:
            self.flip(0)
            print('flip')
        # randomly flip the array

class PalmTree(AsciiCanvas):
    def __init__(self, width, height):
        x_pad=3
        trunk_height_factor = np.random.uniform(0.5, 0.75)
        trunk_height = max(int(height * trunk_height_factor), 4)


        direction = np.random.choice(['left', 'right'])
        # direction = 'center'
        trunk = PalmTrunk(width, trunk_height, direction, x_pad)
        trunk_offset = (0, height-trunk_height)
        self.add_element(trunk, trunk_offset)
        print('tH', trunk_height)

        lower_leaves = np.random.randint(2, 5)
        offset = [x_pad, 0]
        if direction == 'left':
            offset[0] = 0
        elif direction == 'right':
            offset[0] = int(width/2)-1

        crown_height = height - trunk_height + lower_leaves
        print('add_crown')
        print('offset', offset)
        self.add_element(PalmCrown(width-x_pad, crown_height, lower_leaves), offset)
        print(self)

        print('_'*20)
        # exit()

class PalmForest(AsciiCanvas):
    def __init__(self, width, height, n_trees, min_h, max_h, **kwargs):

        coords = TreeCoords(width, height, n_trees, **kwargs).coords

        for coord in coords:
            height = np.random.randint(int(min_h/2), int(max_h/2))*2
            tree = PalmTree(height, height)
            self.add_element(tree, coord)
        # print(self)
