import random


def insertion_sort(size):

    # Create a randomized array to sort.
    array = []
    for a in range(0, size):
        array.append(random.randint(1, size))
    print('Unsorted Array: ' + str(array))

    # Count number of steps it took to sort the entire array.
    counter = 0

    # For each item from second array element on...
    for x in range(1, len(array)):
        key = array[x]
        y = x - 1

        while y >= 0 and array[y] > key:
            counter = counter + 1
            array[y+1] = array[y]
            y = y - 1
            array[y+1] = key

    print('Sorted Array: ' + str(array))
    print('Number of steps to sort: ' + str(counter))
    return None
