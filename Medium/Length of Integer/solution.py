import sys

def solve(args):
    num = abs(int(args.pop()))
    
    get_len = lambda n: 1 + get_len(n//10) if (n > 0) else n 
    return get_len(num) if num != 0 else 1

if __name__ == '__main__':
    result = solve(sys.argv[1:])
    print(result)