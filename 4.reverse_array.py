# Array Reverse Recursion (In-place or Non In-place):
# Define a recursive function that takes an array as input.
# Swap the first and last elements.
# Recursively call the function with the remaining subarray.
def rev_arr(arr,start,end):
    if start>end:
        return
    arr[start],arr[end]=arr[end],arr[start]
    rev_arr(arr,start+1,end-1)
    
arr=[1,2,3,4,5]
rev_arr(arr,0,4)
print(arr)
        