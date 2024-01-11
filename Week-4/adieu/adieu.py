import sys
import inflect
a = inflect.engine()

List = []

while True:
    try:
        names = input("Name: ").title()
        if len(names) < 1:
            sys.exit()

        List.append(names)
        output = a.join(List)

    except EOFError:
        print('\n')
        print("Adieu, adieu, to " + output)
        break
    else:
        continue
