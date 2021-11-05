x = 100  # GLOBAL variable
MAX_TRIES = 5

def spam():
    y = 42   # LOCAL variable
    x = 50
    print("in spam(): x is", x)

spam()
# print("in main: y is", y)  INVALID
print("in main: x is", x)