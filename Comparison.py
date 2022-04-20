from Selection_Sort import selection_sort
from Insertion_Sort import insertion_sort
from Quick_Sort     import quicksort

import random
import time

unsorted_list = [random.randint(0, 100000) for _ in range(10000)]
# print("Before Selection Sort\t: ", unsorted_list)

time_start = time.time()
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