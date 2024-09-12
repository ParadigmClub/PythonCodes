# Define the list for examples
example_list = [1, 2, 3, 4, 5]

# list() - Returns a list created from the passed arguments, which should be a sequence type (string, list, tuple, etc.). If no argument is passed, it will create an empty list.
example_sequence = "Hello"
print(list(example_sequence))  # Output: ['H', 'e', 'l', 'l', 'o']

# append() - Adds a single item to the end of the list.
example_list.append(6)
print(example_list)  # Output: [1, 2, 3, 4, 5, 6]

# extend() - Adds one list at the end of another list.
example_list.extend([7, 8])
print(example_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# insert() - Adds an element at a specified index.
example_list.insert(2, 'a')
print(example_list)  # Output: [1, 2, 'a', 3, 4, 5, 6, 7, 8]

# reverse() - Reverses the order of the elements in a list.
example_list.reverse()
print(example_list)  # Output: [8, 7, 6, 5, 4, 3, 'a', 2, 1]

# index() - Returns the index of the first matched item from the list.
print(example_list.index('a'))  # Output: 6

# len() - Returns the length of the list i.e. number of elements in a list.
print(len(example_list))  # Output: 9

# sort() - Sorts the items of the list.
example_list = [3, 1, 4, 2, 5 ]
example_list.sort()
print(example_list)  # Output: [1, 2, 3, 4, 5]
example_list.reverse() # Output: None
print(example_list)  # Output: [5, 4, 3, 2, 1]

# clear() - Removes all the elements from the list.
example_list.clear()
print(example_list)  # Output: []

# count() - Counts how many times an element has occurred in a list and returns it.
example_list = [1, 2, 2, 3]
print(example_list.count(2))  # Output: 2

# sorted() - Returns a newly created sorted list; it does not change the passed sequence.
example_list = [3, 1, 2]
print(sorted(example_list))  # Output: [1, 2, 3]

# pop() - Removes the element from the specified index and also returns the element which was removed.
example_list = [1, 2, 3, 4, 5]
print(example_list.pop(2))  # Output: 3
print(example_list)  # Output: [1, 2, 4, 5]

# remove() - Used when we know the element to be deleted, not the index of the element.
example_list.remove(4)
print(example_list)  # Output: [1, 2, 5]

# max() - Returns the element with the maximum value from the list.
example_list = [1, 2, 3]
print(max(example_list))  # Output: 3

# min() - Returns the element with the minimum value from the list.
print(min(example_list))  # Output: 1

# sum() - Returns the sum of elements of the list.
print(sum(example_list))  # Output: 6