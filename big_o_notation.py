# BigO(n) - Linear Time complexity
# BigO(n ^ 2) - Quadriatic Time complexity
# BigO(logn) - Logarithamic Time complexity

# time & space complexity fo assigning a value to a variable is always Bigo(1)

# BigO(1) - Linear time complexity
def multi(n):
    return n * n


# BigO(n) - Linear time complexity
# As input grows, no of times operations performed also grows
def print_n(n):
    for i in range(n):
        print(i)


print_n(5)
print_n(50)


# Dropping constants
# this Gives n + n = 2n, 2 a constant is Omitted
def print_n(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)


# BigO(n ^ 2) - Linear time complexity
def print_n(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


# Removing non dominant term
# remove the non dominant term n from (n^2 + n), os only n ^ 2 remains
def print_n(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


# divide and conquer uses BigO(logN)
# logarithmic time complexity
# Ex: Binary Search, Binary Search Trees (BST) Operations
# highly efficient, particularly for large input sizes


# Space complexity
# since the func is getting called recursively, it aqdds the function into stack memoery like sum(3), sum(2), sum(1), so SPace complexity is BigO(n)
def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)


# Bigo(1) space complexity
# simple operations to hold the results
def check_even(n):
    is_even = n % 2 == 0
    result = n + 2
    return is_even, result


# Exception Case of addition & Multiply
# time complexity will be BigO(a) + BigO(b)
def aa_add(a, b):
    for i in a:
        print(i)

    for i in b:
        print(i)


# time complexity will be BigO(a) * BigO(b)
def aa_mul(a, b):
    for i in a:
        for j in b:
            print(i, j)


