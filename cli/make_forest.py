#!/usr/bin/env python3
import os
import argparse
from treez import Forest

NVIM = '''
░▒█▄░▒█░▒█▀▀▀░▒█▀▀▀█░▒█░░▒█░▀█▀░▀█▀░▒█▀▄▀█
░▒█▒█▒█░▒█▀▀▀░▒█░░▒█░░▒█▒█░░▒█░░▒█░░▒█▒█▒█
░▒█░░▀█░▒█▄▄▄░▒█▄▄▄█░░░▀▄▀░░▄█▄░▄█▄░▒█░░▒█
'''

NVIM = '''
┏━┓━┏┓┏━━━┓┏━━━┓┏┓━━┏┓┏━━┓┏━━┓┏━┓┏━┓
┃┃┗┓┃┃┃┏━━┛┃┏━┓┃┃┗┓┏┛┃┗┫┣┛┗┫┣┛┃┃┗┛┃┃
┃┏┓┗┛┃┃┗━━┓┃┃━┃┃┗┓┃┃┏┛━┃┃━━┃┃━┃┏┓┏┓┃
┃┃┗┓┃┃┃┏━━┛┃┃━┃┃━┃┗┛┃━━┃┃━━┃┃━┃┃┃┃┃┃
┃┃━┃┃┃┃┗━━┓┃┗━┛┃━┗┓┏┛━┏┫┣┓┏┫┣┓┃┃┃┃┃┃
┗┛━┗━┛┗━━━┛┗━━━┛━━┗┛━━┗━━┛┗━━┛┗┛┗┛┗┛
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'''
def parse_args():
    EXAMPLES = '''Examples:
                    make_forest.py 8 -w 80 40 -p 5 5 --max_h 20 --ratio 0.25 --scale 0.15'''
    parser = argparse.ArgumentParser(description='Ascii tree generator',
                                     formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument('n_trees', default= 8, type=int, nargs='?',
                        help='Number of trees')
    parser.add_argument('-w', '--win-size', default=os.get_terminal_size(), type=int,
                        nargs=2, help='Window size (px)')
    parser.add_argument('-p', '--padding', default=5, type=int,
                        nargs=2, help='Border padding for tree trunk (px)')
    parser.add_argument('--max_h', default=10, type=int,
                        help='Max tree height(px)')
    parser.add_argument('--min_h', default=5, type=int,
                        help='Max tree height(px)')
    parser.add_argument('--method', default='lhc',
                        help='Method for calculating Tree coordinates')
    return parser.parse_args()


def main(inps):


    print(inps)

    forest = Forest(*inps.win_size,
                    n_trees=inps.n_trees,
                    min_h=inps.min_h,
                    max_h=inps.max_h,
                    method=inps.method)
    print(forest)


if __name__ == '__main__':
    inps = parse_args()
    main(inps)

