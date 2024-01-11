def main():
    c = input("Enter a variable name in camel case: ")
    s = convert(c)
    print(f"Snake case variable: {s}")

def convert(c):
    s = ""
    for i in c:
        if i.isupper():
            s += '_' + i.lower()
        else:
            s += i
    return s

if __name__ == "__main__":
    main()
