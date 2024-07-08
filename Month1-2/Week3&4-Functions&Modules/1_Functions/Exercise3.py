# Write a lambda (anonymous) function to sort a list of tuples by the second value.

tuples_list = [(1, 3), (4, 1), (5, 2), (2, 7)]

sorted_tuple_list = sorted(tuples_list, key=lambda x: x[1])

print(sorted_tuple_list) # Output: [(4, 1), (5, 2), (1, 3), (2, 7)]