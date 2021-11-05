from john.math import geo
# from john/math import geo.py
#  find john/math/geo.py in sys.path

# virtual environment

print(geo.circle_area(15))
print(geo.rectangle_area(5, 19))
print(geo.ANIMAL)
# geo._help_function()

# module search order
# 1. current folder
# 2. folders in PYTHONPATH
# 3. folders in installation folder
import sys
for path in sys.path:
    print(path)
