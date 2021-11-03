list1 = list()   #  List list1 = new List();
x = 5
y = "gadzooks"
list2 = [1, 2, x, 3, 'a', 'b', 'c', y, None, True, 5.9]
list3 = [1, 2, 3, 4]
list4 = ['alpha', 'beta',  'gamma', 'delta']
list5 = []

cities = ['Houston', 'Columbus', 'Chicago', 'Jersey City',
          'Wilmington']
print(cities[0], cities[3], cities[-1])
# cities[len(cities) - 1]
cities.append('Plano')
print(cities)
cities.append('Dallas')
print(cities)
cities.insert(0, 'Richmond')
print(cities)
cities.insert(4, 'Durham')
print(cities)
more_cities = ['Paris', 'London', 'Bangalore', 'Tel Aviv']
cities.extend(more_cities)
print(cities)
# LIST.append(obj)  LIST.insert(pos, obj)
# LIST.extend(interable)
del cities[0]
print(cities)
# cities.append(cities)
d = cities.pop(3)
print(d, cities)
t = cities.pop()
print(t, cities)
cities.remove('Jersey City')
print(cities)
# cities.remove('Seattle') raises ValueError
# city = 'Seattle'
# if city in cities:
#     cities.remove(city)
#  del LIST[pos]  LIST.pop()  LIST.pop(pos)  LIST.remove(value)
print(cities[0:3])  # start at 0, plus 3 items
print(cities[2:4])  # start at 2, plus 2 items
print(cities[:2])  # first 2  [0:2]
print(cities[5:])  # [5:len(cities)]
print(cities[3:7])
print()

for city in cities:
    # city = cities[0]
    # city = cities[1]
    # ...
    print(city)
print()

s = 'abc'
for letter in s:
    print(letter)
print()

for language in 'Python',  'Perl', 'Java', 'Kotlin':
    print(language)
print()

for value in 2, 6, 8, 'wildebeest':
    print(value)
print()

# namedtuple
# dataclasses

a = 39000
b = 365
print(divmod(a, b))

print(cities)
for city in cities:   # for == foreach
    print(city)
print()

# for i in range(len(cities)):
#     print(i, cities[i])
# print()

for i, city in enumerate(cities):
    print(i, city)
print()
print(list(enumerate(cities)))


