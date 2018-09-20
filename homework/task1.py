import argparse

from probability import prob

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', dest='n', required=True, type=int)
    result = parser.parse_args()
    print('Even number probability', prob(result.n))