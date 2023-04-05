# Define a function called selection_sort that takes an array as input
def selection_sort(array):
    # Set n to the length of the input array
    n = len(array)
    
    # Loop over each element in the array
    for i in range(n):
        # Set the minimum index to the current index of the outer loop iteration
        min_index = i
        
        # Loop over each element in the unsorted portion of the array
        for j in range(i+1, n):
            # If the value at the current minimum index is greater than the value at the current index of the nested loop
            if array[min_index] > array[j]:
                # Update the minimum index to be the index of the current nested loop iteration
                min_index = j
        
        # Swap the values at the current minimum index and the current index of the outer loop
        array[i], array[min_index] = array[min_index], array[i]
    
    # Return the sorted array
    return array


# Define an example list to be sorted
list_to_sort = [64, 25, 12, 22, 11]

# Call the selection_sort function on the example list and assign the sorted list to the variable sorted_list
sorted_list = selection_sort(list_to_sort)

# Print the sorted list to the console
print("Sorted List: ", sorted_list)

#def selection_sort(array):
#    n = len(array)
#    for i in range(n):
#        min_index = i
#        for j in range(i+1, n):
#            if array[min_index] > array[j]:
#                min_index = j
#        array[i], array[min_index] = array[min_index], array[i]
#    return array
