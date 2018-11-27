import binary_search
import simple_search
import insertion_sort
import random
import time

# Generate random sorted array of custom length.
lengthOfArray = 100
array = []
for x in range(lengthOfArray):
    array.append(random.randint(1, 100))
sortedArray = sorted(array)
print("Array: " + str(sortedArray))
arrayLength = len(array)
print("Length of array: " + str(arrayLength))

# Set the number to find in array.
numberToFind = 2
print("Number to find: " + str(numberToFind))
print()

# Do Binary Search
print("=======Binary Search=======")
binarySearchStart = time.perf_counter()
index = binary_search.binary_search(sortedArray, numberToFind)
binarySearchEnd = time.perf_counter()
binarySearchTime = binarySearchEnd - binarySearchStart
print("Time elapsed: " + str(binarySearchTime))
if index is not None:
    print("Index of number: " + str(index))
else:
    print(str(numberToFind) + " could not be found in the array.")
print()

# Do Simple Search
print("=======Simple Search=======")
simpleSearchStart = time.perf_counter()
index = simple_search.simple_search(sortedArray, numberToFind)
simpleSearchEnd = time.perf_counter()
simpleSearchTime = simpleSearchEnd - simpleSearchStart
print("Time elapsed: " + str(simpleSearchTime))
if index is not None:
    print("Index of number: " + str(index))
else:
    print(str(numberToFind) + " could not be found in the array.")
print()

print("=======Conclusion=======")
timeComparison = binarySearchTime-simpleSearchTime
if timeComparison < 0:
    print("See! Binary search IS faster than simple search!")
    print("Faster by: " + str(timeComparison * -1) + " seconds!")
else:
    print("Simple search beat binary search this time... probably because the array was too small.")
    print("Faster by: " + str(timeComparison) + " seconds!")
print()

print("=======INSERTION SORT=======")
insertionSortStart = time.perf_counter()
insertion_sort.insertion_sort(lengthOfArray)
insertionSortEnd = time.perf_counter()
insertionSortTime = insertionSortEnd - insertionSortStart
print("Time elapsed: " + str(insertionSortTime))

