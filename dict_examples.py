d1 = dict()
d2 = {'a': 5, 'm': 19, 'z': 8}
print(d2['m'])
d2['c'] = 47
d2['e'] = 6.9
print(d2)
d3 = {}
del d2['z']
print(d2)
print('m' in d2)
print('x' in d2)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
print(airports['RDU'])
del airports['IAD']
print(airports)
airports['IAH'] = "Houston"
print(airports)
print(len(airports))
print(airports.keys())
print(airports.values())
print(type(airports.keys()))
k = airports.keys()
print(len(k))
print(airports.items())

for code in 'RDU', 'MCO', 'XYZ', 'WOMBAT', 'ABQ', 5, 18.9:
    print(code, airports.get(code, "Not found"))  # airports[code]
print()
more_data = [
    ('MIA', 'Miami'),
    ('SEA', 'Seattle-Tacoma'),
    ('MCO', 'Disney'),
    ('LAX', 'Lost Angels'),
    ('MCI', 'Kansas City, KS'),
]
for code, name in more_data:
    print(airports.setdefault(code, name))
print()
print(airports)
print()

for code, name in airports.items():
    print(code, name)
print()


