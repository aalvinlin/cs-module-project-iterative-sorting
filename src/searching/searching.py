def linear_search(arr, target):
    # Your code here
    for index in range(len(arr)):
        
        current_item = arr[index]

        if target == current_item:
            return index

    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    lower_bound = 0
    upper_bound = len(arr) - 1

    while lower_bound <= upper_bound:

        guess_index = (lower_bound + upper_bound) // 2
        guess = arr[guess_index]

        if guess == target:
            return guess_index

        # current midpoint is too small
        # target would be found in the upper half of the range
        elif guess < target:
            lower_bound = guess_index + 1
        
        # current midpoint is too big
        # target would be found in the lower half of the range
        elif guess > target:
            upper_bound = guess_index - 1

    return -1  # not found
