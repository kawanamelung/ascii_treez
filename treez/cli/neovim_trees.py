#!/usr/bin/env python3

from treez import Forest, Tree

if __name__ == '__main__':
    forest = Forest(tree=Tree,
                        width=40,
                        height=20,
                        n_trees=10,
                        min_h=5,
                        max_h=7,
                        method='lhc')
    print(forest)

