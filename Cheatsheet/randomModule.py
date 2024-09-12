#write one similarly for all functions from random module

import random

import random

# random() - Used to generate a random floating-point number between 0.0 to 1.0, including zero but excluding one.
print(random.random())  # Example Output: 0.022353

# randint() - Used to generate a random number between start and stop where both the numbers are inclusive.
print(random.randint(10, 15))  # Example Output: 12 (could be any number between 10 and 15)

# randrange() - Used to generate a random number in the specified range.
# random.randrange(<stopvalue>) - Generates a random number in the range 0 to <stopvalue>
print(random.randrange(35))  # Example Output: 17 (could be any number between 0 and 34)

# random.randrange(start, stop) - Generates a random number in the range start to stop
print(random.randrange(11, 45))  # Example Output: 29 (could be any number between 11 and 44)

# random.randrange(start, stop, step) - Generates a random number in the range start to stop, with a step value
print(random.randrange(11, 45, 4))  # Example Output: 27 (could be any number like 11, 15, 19, 23, 27, 31, 35, 39, 43)

# choice() - Returns a randomly selected element from a non-empty sequence.
example_list = [1, 2, 3, 4, 5]
print(random.choice(example_list))  # Example Output: 3 (could be any element from the list)

# shuffle() - Shuffles the elements of a list in place.
random.shuffle(example_list)
print(example_list)  # Example Output: [4, 1, 5, 2, 3] (order will be random)

# sample() - Returns a list of unique elements chosen randomly from the population sequence.
print(random.sample(example_list, 3))  # Example Output: [2, 4, 1] (could be any 3 unique elements from the list)

# uniform() - Generates a random floating-point number between the specified range.
print(random.uniform(1.5, 10.5))  # Example Output: 7.234 (could be any floating-point number between 1.5 and 10.5)

# seed() - Initializes the random number generator with a seed value.
random.seed(10)
print(random.random())  # Example Output: 0.5714025946899135 (will be the same every time the seed is set to 10)
