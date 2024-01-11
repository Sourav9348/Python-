def remove_vowels(text):
    vowels = "aeiouAEIOU"
    text_without_vowels = "".join(i for i in text if i not in vowels)
    return text_without_vowels

def main():
    user_text = input("Input: ")
    result = remove_vowels(user_text)
    print(f"Output: {result}")

if __name__ == "__main__":
    main()
