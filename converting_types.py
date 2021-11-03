#  int float str bool
#  bytes list tuple dict set
x = 5   #  int x = new int(5);
print(type(x), type(int))

x = int()  # new instance of int
print(x)

a = 1.234
aa = str(a)  # convert float to str
print(aa)
print(len(aa))
print(type(a), type(aa))

a = "123"
b = 456
print(a + str(b))
print(int(a) + b)

#  str(any-object)
#  bool(any-object)

#  int(num-or-integer-string)
#  float(num-or-numeric-string)

#  list(any-iterable)
#  tuple(any-iterable)
#  set(any-iterable)
#  dict(any-iterable-of-pairs)

class Car:
    def __init__(self, model, color):
        self._model = model
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def model(self):
        return self._model

    def __repr__(self):
        return f"Car('{self.model}', '{self.color}')"

    def __str__(self) -> str:
        return f"{self.color} {self.model}"


c1 = Car('Prius', 'red')

print("attributes:", c1.color, c1.model)
print("object:", c1)   # print(str(c1))
print(repr(c1))






