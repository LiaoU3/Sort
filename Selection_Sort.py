import random
def selection_sort(nums:list):
    for i in range(len(nums)):
        min_val = nums[i]
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < min_val:
                min_val = nums[j]
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

def main():
    unsorted_list = [random.randint(0, 100) for _ in range(10)]
    print("Before Selection Sort\t: ", unsorted_list)
    print("After Selection Sort\t: ", selection_sort(unsorted_list))
    
if __name__ =="__main__":
    main()