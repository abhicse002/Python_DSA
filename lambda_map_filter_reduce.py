# From a list of numbers, calculate square on the list elements & return the numbers which are even only (Use lambda, map & filter all 3)

from functools import reduce
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
sq_list = list(map(lambda x: x**2, num))

filtered_l = list(filter(lambda x: x % 2 == 0, sq_list))
print(filtered_l)

reduced = reduce(lambda x, y: x + y, filtered_l)
print(reduced)
