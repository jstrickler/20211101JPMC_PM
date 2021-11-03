fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

#  [EXPR for VAR in ITERABLE if CONDITION]
f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

f4 = [f for f in fruits if len(f) > 7]
print("f4:", f4, '\n')

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'eggs', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'dosi', 'spam', 'spam', 'spam',
        'spam', 'tacos', 'spam', 'spam', 'spam', 'spam', 'spam', ]

good_food = [f for f in food if f != 'spam']
print("good_food:", good_food, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
dobs = [p[3] for p in people]
print("dobs:", dobs, '\n')

x = [1.239093, 2.39029302, 8.839082083]
rounded = [round(n, 2) for n in x]
print("rounded:", rounded, '\n')

rounded = list(map(lambda n: round(n, 2), x))
print("rounded:", rounded, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

fgen = (f.upper() for f in fruits)
print("fgen:", fgen, '\n')
for fruit in fgen:
    print(fruit, end=' ')
print('\n')

