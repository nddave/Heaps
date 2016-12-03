# Heaps

![alt tag](https://raw.githubusercontent.com/nddave/Heaps/master/Heaps.png)

An implementation of d-ary heaps using Python3, where 'd' is defined by the user.

# Getting started

[Heaps](https://github.com/nddave/Heaps/blob/master/heaps.py) is quick and easy to setup. You do not need any additional libraries than the ones built into Python3. So, download the Heaps.zip file, change directory to the Heaps folder and run it with the following command:
```
python3 heaps.py 100 2
```
Here we see that the system argument indexed at one, is "100" and the system argument indexed at two, is "2". The first system argument is the size of the heap. Meaning, how big do you want the heap to be? And the second system argument is the branching factor of your heap. Given these two values, the program will create a heap with the satisfied conditions with n random items, that all, follow the heap property.

Once the heap of size n and branching factor d is created (where n and d are user defined values, and heap data is made up of random integer values), the program then runs heap sort and insertion sort on the same and returns juxtaposed time outputs. The program can easily handle upto infinately many values and heapsort it in O(nlog(n)) time. So, for the above command, it gives the following output:

```
Generating 100 random numbers
====
starting heapSort test
Heapsort took 0.001229 seconds
====
starting insertionSort test
Insertion sort took 0.001384 seconds
```

# License information ![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). 

Program is created by [Nirman Dave](http://www.nirmandave.com) as a form of assignment for *Data Structures and Algorithms 1 COSC201* course at *Amherst College, Amherst MA* under *Professor James Glenn*.
