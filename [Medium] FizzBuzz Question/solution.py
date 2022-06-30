import sys

def solve(args):
    num = int(args.pop())
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

if __name__ == '__main__':
    result = solve(sys.argv[1:])
    print(result)