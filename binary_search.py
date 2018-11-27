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
