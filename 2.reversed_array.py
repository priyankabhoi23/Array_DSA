# Array Reverse Using a Loop (In-place):
# Iterate through the array using two pointers (start and end).
# Swap elements at the start and end pointers.
# Move the start pointer towards the end and the end pointer towards the start until they meet or cross each other.
arr=[1,2,3,4,5]
def arr_rev(arr,start,end):
    while start < end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
arr_rev(arr,0,4)
print(arr)