<<<<<<< HEAD
from copy import copy
from Selection_Sort import selection_sort
from Insertion_Sort import insertion_sort
from Quick_Sort     import quick_sort
from Merge_Sort     import merge_sort
=======
from Selection_Sort import selection_sort
from Insertion_Sort import insertion_sort
from Quick_Sort     import quicksort
>>>>>>> 717ded4590b997f90347a13315224fb86bacae00

import random
import time

unsorted_list = [random.randint(0, 100000) for _ in range(10000)]
# print("Before Selection Sort\t: ", unsorted_list)

time_start = time.time()
<<<<<<< HEAD
sorted_list = selection_sort(unsorted_list.copy())
time_end = time.time()
print(selection_sort.__name__ + " " + ('Wrong !' if sorted_list != sorted(unsorted_list.copy()) else "Correct !"))
print("Running time :", time_end - time_start)
print("---------------------------------")

time_start = time.time()
sorted_list = insertion_sort(unsorted_list.copy())
time_end = time.time()
print(insertion_sort.__name__ + " " + ('Wrong !' if sorted_list != sorted(unsorted_list.copy()) else "Correct !"))
print("Running time :", time_end - time_start)
print("---------------------------------")

time_start = time.time()
sorted_list = quick_sort(unsorted_list.copy())
time_end = time.time()
print(quick_sort.__name__ + " " + ('Wrong !' if sorted_list != sorted(unsorted_list.copy()) else "Correct !"))
print("Running time :", time_end - time_start)
print("---------------------------------")

time_start = time.time()
sorted_list = merge_sort(unsorted_list.copy())
time_end = time.time()
print(merge_sort.__name__ + " " + ('Wrong !' if sorted_list != sorted(unsorted_list.copy()) else "Correct !"))
print("Running time :", time_end - time_start)
print("---------------------------------")
=======
selection_sort(unsorted_list.copy())
# print("After Selection Sort\t: ", selection_sort(unsorted_list))
time_end = time.time()
print(time_end - time_start)

time_start = time.time()
insertion_sort(unsorted_list.copy())
# print("After Insertion Sort\t: ", insertion_sort(unsorted_list))
time_end = time.time()
print(time_end - time_start)

time_start = time.time()
quicksort(unsorted_list.copy(), 0, len(unsorted_list) - 1)
# print("After Quick Sort\t: ", quicksort(unsorted_list, 0, len(unsorted_list) - 1))
time_end = time.time()
print(time_end - time_start)
>>>>>>> 717ded4590b997f90347a13315224fb86bacae00
