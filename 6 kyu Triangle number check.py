def is_triangle_number(number):
    if type(number) != int:
        return False
    row = 1
    while number > 0:
        number -= row
        row += 1
    return number == 0
