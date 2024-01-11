while True:
    try:
        fuel_input = input("Fraction: ")
        x, y = fuel_input.split("/")
        fuel_percent = (int(x) / int(y)) * 100
        if fuel_percent <= 1:
            print("E")
            break
        elif int(x) > int(y):
            pass
        elif fuel_percent >= 99:
            print("F")
            break
        else:
            print(round(fuel_percent),"%", sep="")
            break
    except (ValueError, ZeroDivisionError):
        pass
