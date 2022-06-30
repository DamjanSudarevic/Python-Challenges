import sys

def solve(args):
    string = args.pop().replace("{", "").replace("}", "")
    fields = string.split(",")

    product = {}
    for field in fields:
        [key, value] = field.split(":")
        dict_key = key.strip("\'").replace("\"", "")
        product[dict_key] = float(value.strip("\'"))
    
    return round((product["sell_price"] - product["cost_price"])* product["inventory"])

if __name__ == '__main__':
    result = solve(sys.argv[1:])
    print(result)