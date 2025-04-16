import numpy as np
#printing the full array
array = np.random.randint(1,51, size =(5,5), dtype=int)
print("Full array:")
print(array)

#printing the number from the second row, third column
print("Element at 2nd row, 3rd column:")
print(array[1,2])

#printing sum of all elements in array
print("Sum of all elements:")
print(np.sum(array))

#printing mean of each row
print("Mean of each row:")
print(np.mean(array, axis=1))

#printing the max value of each column
print("Max value of each column:")
print(np.max(array, axis=0))

