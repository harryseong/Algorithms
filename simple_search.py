def simple_search(array, number):
    counter = 0
    for x in range(len(array)):
        counter = counter + 1
        if array[x] == number:
            return x
    print('# of Steps: ' + str(counter))
    return None
