import sys

def calculate(op, x, y):
    if op == 'add':
        return x + y
    elif op == 'sub':
        return x - y
    elif op == 'mul':
        return x * y
    elif op == 'div':
        if y == 0: return "Error: Division by zero"
        return x / y
    else:
        return "Unknown operation"

if __name__ == "__main__":
    # Expecting arguments: python app.py add 5 10
    if len(sys.argv) != 4:
        print("Usage: python app.py <op> <x> <y>")
        sys.exit(1)

    op = sys.argv[1]
    x = float(sys.argv[2])
    y = float(sys.argv[3])
    
    print(calculate(op, x, y))
