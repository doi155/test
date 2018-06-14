import sys


def foo():
    print(os.path.cwd())


def test():
    print('test desuyo', file=sys.stdout)
    print(foo())


if __name__ == '__main__':
    test()
