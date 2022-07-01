import sys

def solve(args):
    args = list(map(lambda arg: int(arg), args))
    even_nums = filter(lambda n: n % 2 == 0, args)
    odd_nums  = filter(lambda n: n % 2 != 0, args)
    
    return [sum(even_nums), sum(odd_nums)]

if __name__ == '__main__':
    result = solve(sys.argv[1:])
    print(result)