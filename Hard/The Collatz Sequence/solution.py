import sys

next = lambda x: x//2 if (x%2==0) else x*3+1
collatz = lambda n: [n] + collatz(next(n)) if n != 1 else [n]

def solve(args):
    n = int(args.pop())
    return (max(collatz(n)), collatz(n))

if __name__ == '__main__':
    (result, collatz_sequence) = solve(sys.argv[1:])
    print(f"{result}\n# Collatz sequence: {collatz_sequence}")