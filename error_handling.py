
file_name = "wombats.txt"

try:
    with open(file_name) as file_in:
        pass
except FileNotFoundError as err:
    print(err)


number = 23
values = 5, 8, 0, 4, 10
for v in values:
    try:
        result = number / v
    except (ZeroDivisionError, TypeError) as err:
        print(err)
    except ValueError as err:
        print(err)
    except Exception as err:
        # log exception
        print(err)
    else:  # no exceptions
        print(result)
    finally:  # exceptions or not....
        pass




