i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    name = input("Enter your name (or q to quit): ")
    if name == 'q':
        print("Goodbye!")
        break  # exit loop
    if name == '':
        print("Please enter your name")
        continue  # go directly back to top

    print(f"Hi, {name}")
