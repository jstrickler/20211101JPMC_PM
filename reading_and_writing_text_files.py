file_path = "DATA/mary.txt"

# modes: r w a x  rb wb ab xb

mary_in = open(file_path, 'r')
print(mary_in)
mary_in.close()

with open(file_path) as mary_in:
    for raw_line in mary_in:  # mary_in.readline()
        line = raw_line.rstrip('\n')  # remove \n etc
        print(line)
print("-" * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()  # read entire file
    print("normal:")
    print(contents)
    print("repr:")
    print(repr(contents))
print("-" * 60)

with open(file_path) as mary_in:
    lines = mary_in.readlines()
    print("lines:")
    print(lines)
print("-" * 60)

with open(file_path) as mary_in:
    lines_without_nl = [line.rstrip() for line in mary_in]
    print("lines without NL:")
    print(lines_without_nl)
print("-" * 60)

target = 'q'
file_name = 'DATA/words.txt'
with open(file_name) as words_in:
    count = 0
    output_file_name = f"{target}_words.txt"
    with open(output_file_name, 'w') as file_out:
        for raw_line in words_in:  # for str in file_obj
            if target in raw_line:
                line = raw_line.rstrip()
                count += 1
                file_out.write(raw_line)
                print(line)
print(f"{target} occurs on {count} lines")

file_path = 'DATA/knights.txt'
with open(file_path) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        print(title, name)
print('=' * 60)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')



