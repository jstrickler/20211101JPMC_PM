actor = "Chris Hemsworth"
print(len(actor))    # NOT actor.length()
print(actor)
print(actor.upper())
a1 = actor.upper()
print(actor)
#  .upper() .lower() .capitalize()  .title()
print("this is a test".title())
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))
print()
print(actor)
print(actor.find('Chris'))
print(actor.find('worth'))
print(actor.find('Liam'))
print()

s = "       All my exes live in Texas       "
print("|" + s.lstrip() + "|")  # removes " \t\n\c\f\b"
print("|" + s.rstrip() + "|")  # handy for lines from file
print("|" + s.strip() + "|")
print()

s = "xxxxxxxyxxxxxxxyAll my exes live in Texasyyyyyxyyyyyyx"
print("|" + s.lstrip("xy") + "|")  # removes "xy"  "x" OR "y"
print("|" + s.rstrip("xy") + "|")  # handy for lines from file
print("|" + s.strip("xy") + "|")
print()

raw_line = "Mary had a little lamb\n"
cooked_line = raw_line.rstrip('\n')
print(cooked_line)

print(actor)
print(actor.replace('Chris', 'Liam'))
s = "Mary had a little lamb"
print(s.replace('a', 'X'))
print(s.replace('a', 'X', 2))

name_data = "Lucy     Ricky\tFred Ethel"
names = name_data.split()
print(names)
print(", ".join(names))

x = "fee:fi:fo:fum"
print(x.split(':'))








