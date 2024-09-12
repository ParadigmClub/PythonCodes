# Define the tuple for examples
example_tuple = (1, 2, 3, 4, 5)

# len() - Returns the length of the tuple i.e. number of elements in a tuple.
print(len(example_tuple))  # Output: 5

# count() - Counts how many times an element has occurred in a tuple and returns it.
example_tuple = (1, 2, 2, 3)
print(example_tuple.count(2))  # Output: 2

# index() - Returns the index of the first matched item from the tuple.
print(example_tuple.index(2))  # Output: 1

# max() - Returns the element with the maximum value from the tuple.
example_tuple = (1, 2, 3)
print(max(example_tuple))  # Output: 3

# min() - Returns the element with the minimum value from the tuple.
print(min(example_tuple))  # Output: 1

# sum() - Returns the sum of elements of the tuple.
print(sum(example_tuple))  # Output: 6

# sorted() - Returns a newly created sorted list; it does not change the passed sequence.
example_tuple = (3, 1, 2)
print(sorted(example_tuple))  # Output: [1, 2, 3]

# tuple() - Converts a sequence (string, list, etc.) to a tuple.
example_sequence = "Hello"
print(tuple(example_sequence))  # Output: ('H', 'e', 'l', 'l', 'o')

# Concatenation - Combines two tuples.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition - Repeats the elements in a tuple a specified number of times.
print(tuple1 * 2)  # Output: (1, 2, 3, 1, 2, 3)

# Membership - Checks if an element is in a tuple.
print(2 in tuple1)  # Output: True

# Iteration - Iterates through the elements in a tuple.
for item in tuple1:
    print(item)
# Output:
# 1
# 2
# 3

# Slicing - Accesses a range of elements in a tuple.
example_tuple = (1, 2, 3, 4, 5)
print(example_tuple[1:4])  # Output: (2, 3, 4)