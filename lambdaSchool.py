def lambda_school(n):
    # Your code here
    answer = []
    # loop up to n, using `range`
    # keep in mind we want 1-indexed numbers, instead of 0-indexing
    for num in range(1, n+1):
        # we need to check if num is divisible by 3
        divisible_by_3 = (num % 3 == 0)
        # we need to check if num is divisible by 5
        divisible_by_5 = (num % 5 == 0)
        # we need to check if num is divisible by 3 and 5
        # ordering of how we check divisibility of num is important
        if divisible_by_3 and divisible_by_5:
            answer.append("LambdaSchool")
        elif divisible_by_3:
            answer.append("Lambda")
        elif divisible_by_5:
            answer.append("School")
        # for every other number, we need to push it to our answer
        # list, but as a string, instead of as a number
        else:
            answer.append(str(num))
    return answer
print(lambda_school(30))