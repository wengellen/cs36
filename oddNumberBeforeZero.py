# There is a bug in one line of the code. Find it, fix it, and submit.
# Given an array of integers, count the odd numbers before the first (i.e. leftmost) occurrence of zero.
#
# Example
#
# For sequence = [1, 2, 3, 0, 4, 5, 6, 0, 1], the output should be
# oddNumbersBeforeZero(sequence) = 2.
def oddNumbersBeforeZero(sequence):

    result = 0
    for i in range(1, len(sequence)):
        if sequence[i] == 0:
            break
        if sequence[i] % 2 == 1:
            result += 1
    return result
