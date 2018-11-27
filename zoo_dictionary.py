# Python uses dictionaries for key, value pairs, if you were wondering about Python hashmaps...
def zoo_dict():
    # Initiate animal dictionary.
    dictionary = {'lion': 3, 'tiger': 5, 'mouse': 389}

    # Add three seals to dictionary.
    dictionary['seal'] = 3

    # Set array of animal names.
    animals = ['seal', 'lion', 'tiger', 'liger', 'human']

    # Tell me how many of each animal the zoo has.
    for x in animals:
        if x in dictionary:
            print('There are ' + str(dictionary[x]) + ' ' + x + 's in this zoo!')
        else:
            print('Sorry, we don\'t have any ' + x + 's at our zoo!')