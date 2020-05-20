
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    # the pointer for arrA
    a_pointer = 0
    # the pointer for arrB
    b_pointer = 0
    # denotes that the a pointer is at the end
    a_done = False
    # denotes that the b pointer is at the end
    b_done = False
    
    for i in range(len(merged_arr)):
        # if either a or b is at their end, skip this
        if not a_done and not b_done:
            if arrA[a_pointer] < arrB[b_pointer]:
                # A is smaller and should be added next
                merged_arr[i] = arrA[a_pointer]
                # increment a's pointer only if it still
                # has more elements
                if a_pointer < len(arrA) -1:
                    a_pointer +=1
                else:
                    a_done = True
            else:
                # B is smaller and should be added next
                merged_arr[i] = arrB[b_pointer]
                # increment b's pointer only if it still
                # has more elements
                if b_pointer < len(arrB) - 1:
                    b_pointer +=1
                else:
                    b_done = True
        else:
            if not a_done:
                merged_arr[i] = arrA[a_pointer]
                if a_pointer < len(arrA) -1:
                    a_pointer +=1
                else:
                    a_done = True
            if not b_done:
                 # B is smaller and should be added next
                merged_arr[i] = arrB[b_pointer]
                # increment b's pointer only if it still
                # has more elements
                if b_pointer < len(arrB) - 1:
                    b_pointer +=1
                else:
                    b_done = True

    return merged_arr

def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    mid_index = len(arr) // 2
    
    left = arr[:mid_index]
    right = arr[mid_index:]
    
    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([10, 2, 7, 20, 5, 16, 3, 102, 98]))

def merge_sort_in_place(arr, l=0, r=None):
    # if no argument is given for right,
    if r is None:
        r = len(arr) - 1
    
    # base case
    if len(arr) <= 1:
        return arr
    
    # make a copy of the array that can be used
    # to make comparisons
    copy_arr = arr[:]
    recurse_merge(arr, copy_arr, l, r)
    return arr
    
# had to create an extra function so that
# the array wasn't copied each time
def recurse_merge(arr, copy_arr, start, end):
    # base case
    if start == end:
        return
    # get the middle index
    mid = (start + end) // 2
    # when we call recurse_merge, we swap the
    # arr with the copy_arr.
    # call the recurse on the 'left' side
    recurse_merge(copy_arr, arr, start, mid)
    # call the recurse on the 'right' side
    recurse_merge(copy_arr, arr, mid + 1, end)
    # merge the left and right sides
    merge_in_place(arr, copy_arr, start, mid, end)

# original signature: def merge_in_place(arr, start, mid, end):
def merge_in_place(arr, copy_arr, start, mid, end):
    # the current index we are looking to fill in the array 
    i = start
    # the pointer for the left half.
    a_pointer = start
    # the pointer for the right half
    b_pointer = mid + 1
    # loop while both pointers have not reached their end
    while a_pointer <= mid and b_pointer <= end:
        if copy_arr[a_pointer] < copy_arr[b_pointer]:
            # left value is smaller, and should be added
            arr[i] = copy_arr[a_pointer]
            a_pointer +=1
        else:
            # right value is smaller, and should be added
            arr[i] = copy_arr[b_pointer]
            b_pointer +=1
        # increment in order to move to the next "slot" being considered
        i +=1
    # At this point, either the a or b pointers have reached their end,
    # but it is possible that not both of them have. Therefore we need
    # to continue looping for both independently.
    # Loop a:
    while a_pointer <= mid:
        arr[i] = copy_arr[a_pointer]
        i +=1
        a_pointer +=1
    # Loop b:
    while b_pointer <= end:
        arr[i] = copy_arr[b_pointer]
        i +=1
        b_pointer +=1

print(merge_sort_in_place([180, 10, 2, 7, 20, 5, 16, 3, 102, 98]))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
