import sys
import os
import pprint
import algorithm

def main():
    """docstring for main"""
    print 'Hello, algorithm!\n'
    
    tiny_array = algorithm.read_array_from_file('data/random_integer_array_tiny')
    
    print '== Test insertion sort =='
    print 'Before sorting:'
    print tiny_array
    print 'After sorting:'
    print algorithm.insertion_sort(tiny_array)
    
    arr1 = [1, 2, 6]
    arr2 = [3, 4, 5, 7]
    print algorithm.merge_arrays(arr1, arr2)
    
    arr2 = tiny_array
    print algorithm.merge_sort(arr2)
    
main()
