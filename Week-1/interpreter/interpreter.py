def math_interpreter():
    e = input("Enter an arithmetic expression (e.g., 1 + 1): ")

    x, operator, z = e.split()

    x = int(x)
    z = int(z)

    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        if z != 0:
            result = x / z
        else:
            print("Division by zero is not allowed.")
            return
    else:
        print("please use a valid operator")
        return

    print(f"Result: {result:.1f}")

math_interpreter()
