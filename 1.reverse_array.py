# 1. Array Reverse Using an Extra Array (Non In-place):
# Create a new array of the same size as the original array.
# Copy elements from the original array to the new array in reverse order.
# Input: original_array[] = {4, 5, 1, 2}
# Output: array_reversed[] = {2, 1, 5, 4}
arr=[1,2,3,4,5]
arr2=arr[::-1]
print(arr2)