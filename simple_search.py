def simple_search(array, number):
    counter = 0
    for x in range(len(array)):
        counter = counter + 1
        print(counter)
        if array[x] == number:
            return x
    return None
