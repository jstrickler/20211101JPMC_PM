colors1 = ['red', 'pink', 'purple', 'green', 'blue', 'black']
colors2 = ['pink', 'blue', 'blue', 'blue', 'brown', 'white',
           'black']

s1 = set(colors1)
s2 = set(colors2)
s1.add('orange')
s2.add('yellow')
s2.add('blue')
s2.add('blue')
print("s1:", s1)
print("s2:", s2)

print('common:', s1 & s2)  # intersection
print('not common:', s1 ^ s2) # exclusive-or  (AKA Xor)
print('all:', s1 | s2)  # union
print("just s1:", s1 - s2)
print("just s2:", s2 - s1)
