g = input("Greeting: ").strip().lower()

if g.startswith("hello"):
    print("$0")
elif g.startswith("h"):
    print("$20")
else:
    print("$100")
