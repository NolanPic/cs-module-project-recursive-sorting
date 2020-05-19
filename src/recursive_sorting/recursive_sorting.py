# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    # the pointer for arrA
    a_pointer = 0
    # the pointer for arrB
    b_pointer = 0
    
    for i in range(len(merged_arr)):
        if arrA[a_pointer] < arrB[b_pointer] or b_pointer is -1:
            # A is smaller and should be added next
            merged_arr[i] = arrA[a_pointer]
            # increment a's pointer only if it still
            # has more elements
            if a_pointer < len(arrA) -1:
                a_pointer +=1
            else:
                a_pointer = -1
        else:
            # B is smaller and should be added next
            merged_arr[i] = arrB[b_pointer]
            # increment b's pointer only if it still
            # has more elements
            if b_pointer < len(arrB) - 1:
                b_pointer +=1
            else:
                b_pointer = -1

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

print(merge_sort([10, 2, 7, 5, 16, 3]))

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
