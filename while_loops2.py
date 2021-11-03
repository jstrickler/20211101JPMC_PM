
name = None
while name != 'q':
    name = input("Enter your name (or q to quit): ")
    if name == 'q':
        print("Goodbye!")
    if name == '':
        print("Please enter your name")
    print(f"Hi, {name}")
