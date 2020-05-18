# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # treat the item at index 0 as already sorted
    for i in range(1, len(arr)):
        
        current_unsorted_index = i
        current_unsorted_value = arr[current_unsorted_index]

        # smallest_index = current_unsorted_index

        # compare current item with each item in the sorted section
        # start from the right hand side
        for already_sorted_index in range(0, current_unsorted_index, -1):

            current_sorted_value = arr[already_sorted_index]

            # if the item being palced is smaller than the current item, swap the two
            if current_unsorted_value < current_sorted_value:
                arr[already_sorted_index], arr[current_unsorted_index] = arr[current_unsorted_index], arr[already_sorted_index]
        
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
