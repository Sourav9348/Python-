def convert(input_str):
    converted_str = input_str.replace(":)", "🙂").replace(":(", "🙁")
    return converted_str

def main():
    user_input = input("Are you happy :) or sad :( :- ")
    converted_input = convert(user_input)
    print(converted_input)


main()
