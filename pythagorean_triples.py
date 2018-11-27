def py_trip(arr):
    # Edge case #1: check to ensure that the array is at least 3 members.
    if len(arr) < 3:
        print('False: array is not at least 3 members.')
        return False

    # Edge case #2: check to ensure that all members of the array are non-zero, positives
    for x in arr:
        if x < 1 or x % 1 != 0:
            print('False: mot a positive int.')
            return False

    # Sort array first in ascending order.
    arr.sort()

    # Convert all array members into squares of themselves.
    arrsq = [x**2 for x in arr]

    # Leave 2 for nested for loop.
    for x in range(0, len(arrsq) - 2):

        for y in range(0, len(arrsq) - x - 1):
            if arrsq[len(arrsq) - 1 - x] == arrsq[len(arrsq) - 2 - x] + arrsq[y]:
                print('True!')
                return True

    print('False: array does not contain pythagorean triples.')
    return False