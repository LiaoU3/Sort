from copy import copy
from Selection_Sort import selection_sort
from Insertion_Sort import insertion_sort
from Quick_Sort     import quick_sort
from Merge_Sort     import merge_sort

import random
import time

unsorted_list = [random.randint(0, 100000) for _ in range(10000)]
# print("Before Selection Sort\t: ", unsorted_list)

time_start = time.time()
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