def narcissistic(value):
    z = str(value)
    sum_of_digits = sum(int(i) ** len(z) for i in z)
    return value == sum_of_digits


print(narcissistic(2))


def square_digits(num):
    return int(''.join([str(int(i) ** 2) for i in str(num)]))


print(square_digits(9119))  # 811181
