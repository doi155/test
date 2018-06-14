import sys


def foo():
    print(os.path.cwd())

def test():
    print('test desuyo', file=sys.stdout)  
    print(foo())
    
var test = 0.5f
    
if __name__ == '__main__':
    test()
