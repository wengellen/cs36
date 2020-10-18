def find_lucky(lst):
    # Your code here
    occurrences = {}

    # count number of occurrences for each num in list
    for n in lst:
        if n in occurrences:
            occurrences[n] += 1
        else:
            occurrences[n] = 1

    # add all nums that are possible lucky numbers to a candidates list
    candidates = [key for key, val in occurrences.items() if key == val]

    # return the largest candidate or -1 if there is no lucky number
    if len(candidates) == 0:
        return -1

    return max(candidates)