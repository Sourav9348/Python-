import emoji


user_input = input("Input: ")
user_output = emoji.emojize(user_input, language='alias')

print(f"Output:",user_output)
