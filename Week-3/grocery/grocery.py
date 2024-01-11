dict = {}
while True:
    try:
        grocery = input()
        if grocery in dict:
            dict[grocery] += 1

        else:
            dict[grocery] = 1

    except EOFError:
        print()

        for i in sorted(dict):
            key = i.upper()
            value = dict[i]
            print(f'{value} {key}')
       
        break

