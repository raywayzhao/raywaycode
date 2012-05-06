import sys
import os
import pprint

def devide_array( arr , pos ):
    '''
    Devide a long array 'arr' into two sub-arrays at position 'pos'
    '''
    if pos < len(arr):
        left = arr[:pos]
        right = arr[pos:]
        return left, right
    else:
        sys.stderr.write('Index out of range.')

def insertion_sort( arr ):
    '''
    Implemented according to Cormem's 'Intro2Algorithm'
    Input
        arr - array to be sorted
    '''
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr

def merge_sort( arr ):
    '''
    Merge sort
    '''
    arr_len = len(arr)
    if arr_len == 1:
        return arr
    else:
        half = arr_len/2
        left, right = devide_array(arr, half)
        left, right = merge_sort(left), merge_sort(right) # Recursion
        return merge_arrays(left, right)

def merge_arrays( arr1, arr2 ):
    '''
    Merge two sorted arrays into one
    Input
        arr1 - left array
        arr2 - right array
    '''
    res = []
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] <= arr2[0]:
            res.append(arr1.pop(0))
        else:
            res.append(arr2.pop(0))
    if len(arr1) > 0:
        res += arr1
    if len(arr2) > 0:
        res += arr2
    return res
    
def read_array_from_file( file_name ):
    '''
    Output
        res - the read array list
    '''
    fread = open(file_name, 'r')
    res = []
    for line in fread:
        res.append(int(line.strip()))
    fread.close()
    return res
    