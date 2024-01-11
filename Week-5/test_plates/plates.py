def main():
    s = input("Plate: ")
    result = is_valid(s)
    print(f"Output: {result}")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    for i in range (len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    for c in s:
        if c in [".", " ", "!", "?"]:
            return False

    return True


if __name__ == "__main__":
    main()





