s1 = "spam\n"    # \n \r \t \f \b
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
x = 'spam\\n'
s5 = r"spam\n"

print(s1, s2, s3, s4)
print()

print("It's a Python thing")
print('It is a "Python" thing')
print("It's a \"Python\" thing")  # ugh
print('It\'s a "Python" thing')   # blech
print("""It's a "Python" thing""")  # ahhhhhhh

query = """
select *
from customers
where state = 'tx'
and balance < 10000
order by customer_id desc
"""


