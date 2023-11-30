#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    count = len(sys.argv)
    if count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    ope = sys.argv[2]
    b = int(sys.argv[3])

    if ope == '+':
        result = calculator_1.add(a, b)
    elif ope == '-':
        result = calculator_1.sub(a, b)
    elif ope == '*':
        result = calculator_1.mul(a, b)
    elif ope == '/':
        result = calculator_1.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, ope, b, result))
