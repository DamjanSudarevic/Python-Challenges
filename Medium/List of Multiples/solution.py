import sys

def solve(args):
    [num, length] = map(lambda arg: int(arg), args)
    return [num*i for i in range(length+1) if i > 0]

if __name__ == '__main__':
    result = solve(sys.argv[1:])
    print(result)