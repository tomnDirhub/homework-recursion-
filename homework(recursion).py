def get_multiplied_digits(number):
    str_number = str(number).replace('0', '')
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

print(get_multiplied_digits(901293))