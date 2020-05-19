# TO-DO: complete the helper function below to merge 2 sorted arrays
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


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    mid_index = len(arr) // 2
    
    left = arr[:mid_index]
    right = arr[mid_index:]
    
    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([10, 2, 7, 20, 5, 16, 3, 102, 98]))

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
