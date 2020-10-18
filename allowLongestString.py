# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# Given an array of strings, return another array containing all of its longest strings.
#
# Example
#
# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
def allLongestStrings(inputArray):

    answer = [inputArray[0]]
    for i in range(1, len(inputArray)):
        if len(inputArray[i]) == len(answer[0]):
            answer.append(inputArray[i])
        if len(inputArray[i]) > len(answer[0]):
            answer = ...
    return answer
