#  Array Reverse Stack (Non In-place):
# Push each element of the array onto a stack.
# Pop elements from the stack to form the reversed array.
def rev_arr(arr):
    stack=[]
    for i in arr:
        stack.append(i)
    for i in range(len(arr)):
        arr[i]=stack.pop()
    print(arr, end="")
        
arr=[1,2,3,4,5]
rev_arr(arr)