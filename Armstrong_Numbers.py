def is_armstrong_number(number):
    n = str(number)
    p = len(n)
    sum = 0
    for digit in n:
        sum += int(digit) ** p
    return sum == number
