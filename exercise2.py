# 1 square the list
my_list = [5, 4, 3]

print(list(map(lambda x: x ** x, my_list)))
# 2 List sorting by second item
a = [(0, 2), (5, 2), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)

