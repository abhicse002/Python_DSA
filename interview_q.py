# work if only one number is missing from List
def missing_number(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 10]
n = 10
missing_num = missing_number(arr, n)

print(missing_num)


# works if more than one number is missing from list
def missing_numbers(arr, n):
    for i in range(1, n + 1):
        if i not in arr:
            print(i)

arr = [1, 3, 4, 5, 6, 7, 8, 10]
n = 10

missing_numbers(arr, n)