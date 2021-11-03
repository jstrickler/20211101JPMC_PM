person = 'Bill', 'Gates', 'Microsoft', '1955-10-25'

print(person[0], len(person), type(person))
print(person[0], person[1])

# iterable unpacking
first_name, last_name, product, dob = person
# first_name = person[0]
# last_name = person[1]
# etc etc

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
print(type(people), type(people[0]))
print(people[0])
print(people[0][0])
print()

for person in people:
    # first_name .... = person
    print(person[0], person[1])
print("-" * 60)

for first_name, last_name, product, dob in people:
    print(first_name, last_name)
print('-' * 60)

s1 = ['egg', 'butter', 'cheese']
s2 = 'a', 'b', 'c'
s3 = 'abc'
for obj in s1, s2, s3:
    print(len(obj), type(obj), obj[0], min(obj), max(obj),
          sorted(obj))
print()
r = reversed(s1)
print(r)
for item in r:
    print(item)
print()
print("second loop:")
for item in r:
    print(item)
print(r)