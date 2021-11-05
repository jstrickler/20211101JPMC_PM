import os

def get_message():
    return "Hello, JPMC world"

m = get_message()
print(m)
get_message()  # silly!

def display_message():
    msg = get_message()
    print(msg)
    # return None

display_message()
x = display_message()
print(x)

def toast(a, b):
    return a * b

print(toast(5, 10))
print()

def greet(whom="world"):
    print("Hello,", whom)

greet("Mom")
greet("Dad")
greet()

def find_term(term, *file_paths):
    print("file_paths:", file_paths)
    for file_path in file_paths:
        with open(file_path) as file_in:
            file_name = os.path.basename(file_path)
            for raw_line in file_in:
                if term in raw_line:
                    line = raw_line.rstrip()
                    print(f"{file_name} {line}")

find_term('Lizard', 'DATA/alice.txt')
print()
find_term('pig', 'DATA/alice.txt', 'DATA/parrot.txt', 'DATA/words.txt')
print()
find_term('wombat')
print()
# find_term()  INVALID

def config(**kwargs):
    print(kwargs)
    print()

config(filename='wombats.txt', username='CrocodileDundee', animal="wombat")

def spam(*, foo, bar=12):
    print(foo, bar)

spam(foo=10, bar=20)
spam(bar=8, foo=12)

def wacky(p1, p2=99, *p3, p4, p5="spam", **p6):
    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)
    print("p4:", p4)
    print("p5:", p5)
    print("p6:", p6)
    print()

wacky(100, p4=200)
wacky(100, 200, 300, 400, p5='wildebeest', p4="tractor", file="foo.txt", user="guy")

# python type hinting
# typing module
import typing
def concat(a: str, b: str) -> str:
    return a + b

print(concat('foo', 'bar'))
print(concat(5, 10))
print(concat(['a', 'b'], ['c', 'd']))

# x = concat('a', 'b')
# print(x / 5)