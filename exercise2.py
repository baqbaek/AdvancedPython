# 1 square the list
my_list = [5, 4, 3]

print(list(map(lambda x: x ** x, my_list)))
# 2 List sorting by second item
a = [(0, 2), (5, 2), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
# 3 Comprehensions
second_list = [x for x in 'Bartek']
print(second_list)
# 4 Find duplicates using only comprehensions

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates)
