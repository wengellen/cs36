'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    slot = 0
    for i in range(len(arr)):
        if arr[i] is not 0:
            arr[slot] = arr[i]
            slot += 1

    while slot < len(arr):
        arr[slot] = 0
        slot += 1

    return arr

# arr = [0, 3, 1, 0, -2]
# print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")



# if __name__ == '__main__':
#     # Use the main function here to test out your implementation
#     arr = [0, 3, 1, 0, -2]
#
#     print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")