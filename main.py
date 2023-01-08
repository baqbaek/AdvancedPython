# map, filer, zip, reduce, lambda
from functools import reduce

my_list = [1, 2, 3]
second_list = [10, 20, 30]
third_list = [5, 4, 3]


def multipy(x):
    return x * 2


def check_odd(x):
    return x % 2 != 0


def accumulator(acc, x):
    return acc + x


print(list(map(multipy, my_list)))  # map -> [2, 4, 6]
print(list(filter(check_odd, my_list)))  # filter -> [1, 3]
print(list(zip(my_list, second_list, third_list)))  # zip -> [(1, 10, 5), (2, 20, 4), (3, 30, 3)]
print((reduce(accumulator, my_list, 0)))  # reduce -> 6
print(list(map(lambda x: x * 2, my_list))) # lambda -> [2, 4, 6], its one time function
