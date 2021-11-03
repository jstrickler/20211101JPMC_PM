
person = "Tony Stark"
city = "Los Angeles"
value = 23.30959390347

print(person, city, value)
print()
print(person, city, value, sep="/")
print(person, city, value, sep='')
print(person, end="XX")
print(city, end="XX")
print(value)

line1 = 'wombat\n'
line2 = 'wallaby\n'
print(line1, end='')
print(line2, end='')
print("Done\n")

print(person, "lives in", city)
print("{} lives in {}".format(person, city))
print("The value is {}".format(value))
print("The value is {:.2f}".format(value))
x = 23454643.94
print("{:,.1f}".format(x))
# printf()
print(f"{person} lives in {city}")  # 3.6+
print(f"The value is {value:.2f}")
print(f"Other value is {x:,.1f}")
a = 2
b = 3
print(f"{a} * {b} is {a * b}")




