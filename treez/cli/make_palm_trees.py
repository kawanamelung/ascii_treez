#!/usr/bin/env python3

import os
import argparse
from treez import PalmForest

def parse_args():
    parser = argparse.ArgumentParser(description='Ascii tree generator',
                                     formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument('n_trees', default= 8, type=int, nargs='?',
                        help='Number of trees')
    parser.add_argument('-w', '--win-size', default=os.get_terminal_size(), type=int,
                        nargs=2, help='Window size (px)')
    parser.add_argument('-p', '--padding', default=5, type=int,
                        nargs=2, help='Border padding for tree trunk (px)')
    parser.add_argument('--max_h', default=15, type=int,
                        help='Max tree height(px)')
    parser.add_argument('--min_h', default=10, type=int,
                        help='Max tree height(px)')
    parser.add_argument('--method', default='lhc',
                        help='Method for calculating Tree coordinates')
    return parser.parse_args()


def main(inps):
    inps.width = inps.win_size[0]
    inps.height = inps.win_size[1]

    palms = PalmForest(width=inps.width,
                       height=inps.height,
                       n_trees=inps.n_trees,
                       min_h=inps.min_h,
                       max_h=inps.max_h,
                       method=inps.method)
    print(palms)

if __name__ == '__main__':
    inps = parse_args()
    main(inps)

