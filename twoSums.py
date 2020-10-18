# assume no duplicates in our `nums` array
def two_sum(nums, target):
    # Your code here
    # what about using a dictionary?
    map = {element: index for index, element in enumerate(nums)}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in map:
            return [i, map[diff]]
    return "No two elements sum up to the target"