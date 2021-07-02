def binary_search(sequence,item):

    lower_index = 0
    upper_index = len(sequence)-1

    while len(sequence) != 1:

        half = int(len(sequence)/2)
        first_half = sequence[0:half]
        second_half = sequence[half:len(sequence)]

        if item in first_half:
            sequence = first_half
            upper_index -= half

        elif item in second_half:
            sequence = second_half
            lower_index += half
        else:
            return None

    return lower_index



