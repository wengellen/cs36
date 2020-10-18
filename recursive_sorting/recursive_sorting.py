# TO-DO: complete the helper function below to merge 2 sorted arrays
import math

def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    result = []
    # TO-DO
    while len(arrA) and len(arrB):
        if arrA[0] < arrB[0]:
            result.append(arrA.pop(0))
        else:
            result.append(arrB.pop(0))
        print(result)
    return result + arrA + arrB


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    # find mid point
    # split it into two arrays
    # keep splitting until there is only one elmenet left in the arrays
    # compare the first item from both arrays
    # concat them into a sorted array from small to large
    # merge back left and right array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))




# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
