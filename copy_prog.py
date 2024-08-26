import copy

# l1 = [1, 2, [3, 4]]

# l2 = l1.copy()    # specific to list, cannot be used by other data structures
# l3 = copy.copy(l1)    # can be use for list, dict etc
# l4 = copy.deepcopy(l1)
# l1[2][0] = 8

# print(l1)
# print(l2)
# print(l3)
# print(l4)


dict1 = {'a': 1, 'b': [2, 3]}
dict2 = copy.copy(dict1)    # changes the outer values, but nested objects will be changed, because it copys the references & not values
dict3 = copy.deepcopy(dict2)    # changes the outer values as well as nested objects, because it

dict2['a'] = 9
dict2['b'][0] = 8

print(dict1)
print(dict2)
print(dict3)
