import argparse

from area import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--figure_type', dest='figure_type', required=True, type=str, help='Enter the figure type')
    parser.add_argument('--r', dest='r', type=float, help='Circle radius')
    parser.add_argument('--a', dest='a', type=float, help='Rectangle width')
    parser.add_argument('--b', dest='b', type=float, help='Rectangle height')
    parser.add_argument('--d', dest='d', type=float, help='Triangle width')
    parser.add_argument('--h', dest='h', type=float, help='Triangle height')
    result = parser.parse_args()
    if result.figure_type == 'circle':
        print('Circle area', circle(result.r))
    elif result.figure_type == 'rectangle':
        print('Rectangle area:', rectangle(result.d, result.h))
    elif result.figure_type == 'triangle':
        print('Triangle area:', triangle(result.d, result.h))

