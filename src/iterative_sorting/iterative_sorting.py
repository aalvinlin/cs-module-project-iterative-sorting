# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # treat the item at index 0 as already sorted
    for i in range(1, len(arr)):
        
        current_unsorted_index = i
        current_unsorted_value = arr[current_unsorted_index]
   
        # compare current item with each item in the sorted section
        # start from the right hand side
        for already_sorted_index in range(current_unsorted_index - 1, -1, -1):

            current_sorted_value = arr[already_sorted_index]

            # if the item being palced is smaller than the current item, swap the two
            if current_unsorted_value < current_sorted_value:
                
                arr[already_sorted_index], arr[already_sorted_index + 1] = arr[already_sorted_index + 1], arr[already_sorted_index]
  
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    
    while True:
   
        # keep track of the number of swaps this round
        swaps_this_round = 0

        for i in range(len(arr)):

            current_item = arr[i]

            # compare current item with each item to the right
            for j in range(i + 1, len(arr)):

                item_to_the_right = arr[j]

                # if current item should be moved to the right, swap the items
                # also increment counter for number of swaps
                if current_item > item_to_the_right:

                    arr[i], arr[j] = arr[j], arr[i]
                    
                    swaps_this_round += 1

        # array is sorted if there are no swaps made this round
        if swaps_this_round == 0:
            return arr

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
