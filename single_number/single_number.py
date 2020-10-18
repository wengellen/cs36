'''
Input: a List of integers where every int except one shows up twice
Returns: an integer

Time: O(n) | Space: 0(1)

'''
import time
# O(nLogn) | O(1)
def single_number_pointers(arr):
    start_time = time.time()
    # arr.sort()
    i = 1
    last_item = False
    while i < len(arr):
        if arr[i] != arr[i-1]:
            if last_item:
                end_time = time.time()
                print(f"Two Pointers runtime: {end_time - start_time} seconds")
                return arr[i]
            else:
                end_time = time.time()
                print(f"Two Pointers runtime: {end_time - start_time} seconds")
                return arr[i-1]

        if i == len(arr) - 2:
            # if it's is the last item, [1,1,2,3,3]
            i += 1
            last_item = True
        else:
            i += 2
            use_last = False


# arr = [1, 1, 4, 4, 5, 5 , 6]
arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
# print(f"The odd-number-out is {single_number_pointers(arr)}")

def single_number_pointers_sorted(arr):
    start_time = time.time()
    print(f"Two Pointers Sorted runtime: {  start_time} seconds")
    i = 1
    last_item = False
    while i < len(arr):
        if arr[i] != arr[i-1]:
            if last_item:
                end_time = time.time()
                print(f"Two Pointers Sorted runtime: {end_time - start_time} seconds")
                return arr[i]
            else:
                end_time = time.time()
                print(f"Two Pointers Sorted runtime: {end_time - start_time} seconds")
                return arr[i-1]

        if i == len(arr) - 2:
            # if it's is the last item, [1,1,2,3,3]
            i += 1
            last_item = True
        else:
            i += 2
            use_last = False



# O(n) | O(n)
def single_number(arr):
    start_time = time.time()
    my_dict = {}
    for key in arr:
        if key not in my_dict:
            my_dict[key] = 1
        else:
            my_dict[key] += 1

    for key in my_dict:
        if my_dict[key] == 1:
            end_time = time.time()
            print(f"Hashmap runtime: {end_time - start_time} seconds")
            return key



# arr = [1, 1, 4, 4, 5, 5 , 6]
my_arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
# print(f"The odd-number-out is {single_number(my_arr)}")
