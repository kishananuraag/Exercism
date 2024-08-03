def is_armstrong_number(number):
    str_number = str(number)
    power = len(str_number)
    armstrong_number = 0
    for i in str_number:
        armstrong_number = armstrong_number + int(i)**power
    return number == armstrong_number