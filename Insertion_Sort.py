import random
def insertion_sort(nums:list)->list:
    for i in range(1, len(nums)):
        uninsert = nums[i]
        for j in range(i, -1, -1):
            if uninsert < nums[j-1] and j>0:
                nums[j] = nums[j-1]
            else:
                nums[j] = uninsert
                break
    return nums


def main():
    unsorted_list = [random.randint(0, 100) for _ in range(10)]
    print("Before Selection Sort\t: ", unsorted_list)
    print("After Selevtion Sort\t: ", insertion_sort(unsorted_list))

if __name__ =="__main__":
    main()