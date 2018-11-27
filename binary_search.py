def binary_search(array, number):
    low = 0
    high = len(array)-1
    counter = 0
    while low <= high:
        counter = counter + 1
        mid = int((low + high)/2)
        guess = array[mid]
        if guess == number:
            return mid
        if guess > number:
            high = mid-1
        else:
            low = mid+1

    print('# of Steps: ' + str(counter))
    return None


# Recursive binary search
def binary_search_2(arr, find_this):
    # Edge case #1: Ensure that array length is greater than 0.
    if len(arr) == 0:
        print('Could not find number')
        return False
    if len(arr) % 2 == 1:
        midpoint = (len(arr) + 1) // 2
    else:
        midpoint = len(arr) // 2
    if find_this == arr[midpoint]:
        print('Found ' + str(find_this) + ' in the array!')
        return True
    elif find_this < arr[midpoint]:
        binary_search(arr[0: midpoint], find_this)
    else:
        binary_search(arr[midpoint + 1: len(arr)], find_this)