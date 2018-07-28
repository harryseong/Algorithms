import binary_search
import simple_search
import random
import time

# Generate random sorted array of custom length.
lengthOfArray = 1000000
array = []
for x in range(lengthOfArray):
    array.append(random.randint(1, 200))
sortedArray = sorted(array)
print("Array: " + str(sortedArray))
arrayLength = len(array)
print("Length of array: " + str(arrayLength))

# Set the number to find in array.
numberToFind = 0
print("Number to find: " + str(numberToFind))

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

print("=======Conclusion=======")
timeComparison = binarySearchTime-simpleSearchTime
if timeComparison < 0:
    print("See! Binary search IS faster than simple search!")
    print("Faster by: " + str(timeComparison * -1) + " seconds!")
else:
    print("Simple search beat binary search this time... probably because the array was too small.")
    print("Faster by: " + str(timeComparison) + " seconds!")

