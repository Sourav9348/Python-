def main():
    user_text = input("Input: ")
    result = shorten(user_text)
    print(f"Output: {result}")


def shorten(text):
    vowels = "aeiouAEIOU"
    text_without_vowels = "".join(i for i in text if i not in vowels)
    return text_without_vowels



if __name__ == "__main__":
    main()
