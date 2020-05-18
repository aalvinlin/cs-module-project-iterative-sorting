def linear_search(arr, target):
    # Your code here
    for index in range(len(arr)):
        
        current_item = arr[index]

        if target == current_item:
            return index

    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here


    return -1  # not found
