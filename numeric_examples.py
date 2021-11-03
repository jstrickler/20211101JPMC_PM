
# int float      (bool complex)

i1 = 1234
i2 = 203985209358203985209385209385209358209358209358209358235020258029385029385209385029853029385029835029835029385029385029835029835092835
print(i2 + 1)
i3 = 1_323_930
print(i3)
i4 = 0x1000
i5 = 0b1000
i6 = 0o1000  # diff from C/Java etc   INVALID: 0263
print(i4, i5, i6, '\n')

f1 = 123.456
f2 = 123.
f3 = 0.0
f4 = .30383
f5 = 1.8939e37

a = 23
b = 6
print(a + b, a - b)
print(a * b, a / b, a // b, a // -b)
print(a ** b, a % b)

x = 35.329303
print(round(x, 3))

a += 2  # a = a + 2
a *= 3  # a = a * 3
a /= 5
print(a)

# NOT IMPLEMENTED  a++  ++a   etc

# P E M/D A/S
#  (x + y) * (a - b)
#  x + (y * a) - b
# x + y * a - b






