def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

if __name__ == "__main__":
    print("Simple Calculator")
    print("Enter expressions like 2 + 2 or 5 * 3")

    while True:
        try:
            expression = input("calc> ").strip()
            if expression.lower() in {"quit", "exit", "q"}:
                print("Goodbye")
                break
            if not expression:
                continue

            parts = expression.split()
            if len(parts) != 3:
                print("Usage: number operator number")
                continue

            x_str, op, y_str = parts
            x = float(x_str)
            y = float(y_str)

            if op not in operations:
                print(f"Unsupported operator: {op}")
                continue

            result = operations[op](x, y)
            print(result)
        except ValueError as err:
            print(f"Error: {err}")
        except Exception:
            print("Invalid input. Try again.")
