 # Assignment information
 # ---
 # Class : COSC 201 - Data structures and algorithms
 # Assignment : Programming Project 2
 # Student : Nirman Dave

 # Program information
 # ---
 # Name : Comparing heap sort methods
 # Description : The program lists the time it takes to sort a heap/array of n random elements
 #               with n branches. Where n is defined by the user.
 # Language : Python 3.0

#importing libraries 
import sys
import random
import time

def heapify(heap, index, size, branch):
    """ Rearranges a given heap to maintain its heap property.
    Meaning, that the key of the root node is larger than or 
    equivalent to its childred nodes. This function in specific
    allows for heapify to operate under a heap with n branches;
    where n is defined by the user or by the function in operation.
    """
    left_child = index * branch + 1                                         # finding left child for a parent in a heap with n branches
    if left_child < size:
        largest = left_child                                                # sets largest to left child if it is within the heap
        i = 1                                       
        while (i <= branch-1):                                              # limits the loop to number of branches
            if left_child+i < size and heap[left_child+i] > heap[largest]:  # compares largest to each child under the index parent
                largest = left_child + i                                    # if a child is larger than 'largest', then it is set as 'largest'
                i += 1
            else:
                i += 1
        if heap[index] < heap[largest]:                                     # if parent is smaller than largest,
            swap(heap, index, largest)                                      # then swap largest with the parent
            heapify(heap, largest, size, branch)                            # recur until heapified

def swap(heap, i, j):
    """ Swaps to items in a given heap. Needed during heapify and
    heap sort functions.
    """
    temp = heap[i]
    heap[i] = heap[j]
    heap[j] = temp

def build_heap(heap, branch):
    """ Call heapify starting last node with children and work
    its way backwards.
    """
    i = len(heap) // 2 - 1
    while i >= 0:
        heapify(heap, i, len(heap), branch)
        i = i - 1

def heapsort_test(c, branch):
    """ Test for heap sort. Prints time taken and returns
    a sorted array.
    """
    print("starting heapSort test")
    t = time.process_time()
    heapsort(c, branch)
    print("Heapsort took %f seconds" % ((time.process_time()-t)))
    print("====") 
    return c

def heapsort(arr, branch):
    """ Heap sort works by organizing an array into a heap
    data type with an arbitrary branching factor defined by
    the user. All heaps have the max value on the top, and
    heap sort uses that property to sort by recursively
    arranging max value at the end of the array and re-heapifying
    the remaining values. Algorithm has a O(nlogn) in worst case,
    is in place but not stable.
    """
    end = len(arr)
    start = end // 2 - 1
    for k in range(start, -1, -1):      # for each element from end to start
        heapify(arr, k, end, branch)    # heapify the whole array
    for k in range(end-1, 0, -1):       # for each element from end-1 to start (end-1 as the swapped max value is now at the start of the array)
        swap(arr, k, 0)                 # swap max value with the start of array
        heapify(arr, 0, k, branch)      # re-heapify
            
def insertion_test(c):
    """ Test for insertion sort. Prints time taken and returns
    a sorted array.
    """
    print("starting insertionSort test")
    t = time.process_time()
    insertion_sort(c)
    print("Insertion sort took %f seconds" % ((time.process_time()-t)))
    print("") 
    return c

def insertion_sort(a):
    """ An algorithm that sorts by inserting each element
    one at a time to return a final sorted array. The Algorithm has
    a O(n^2) in worst case, is in-place and stable.
    """
    n = len(a)
    for i in range(1,n):
        t = a[i]
        j = i-1
        while j>=0 and t<a[j]:     # while compares a[i] to last element in sorted side
            a[j+1]=a[j]            # inserts when needed
            j -= 1
        a[j+1]=t
                
def check(a, b):
    """ Verify that all the sorted arrays
    returned by each algorithm are equal.
    """
    if a!=b:
        raise Exception("Sorted arrays don't match")

def do_test(n, branch):
    print("====")
    print ("Generating " + str(n) + " random numbers")
    a = [random.randint(0, 2**30-1) for i in range(n)]
    print("====")  
    t = time.process_time()
    hs_result = heapsort_test(a[:], branch)
    is_result = insertion_test(a[:])
    check(hs_result, is_result)

if __name__=="__main__":
    if len(sys.argv) >= 3:
        n = int(sys.argv[1])
        branch = int(sys.argv[2])
    else:
        print("")
        n = int(input("Enter size: "))
        branch = int(input("Enter branching factor: "))
    do_test(n, branch)