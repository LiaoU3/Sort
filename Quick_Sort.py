import random
def quicksort(nums, left, right):
    if left < right:
        reference = nums[left]
        l = left
        r = right
        while l < r:
            while nums[l] <= reference and l < right:
                l += 1
            while nums[r] >  reference and left < r:
                r -=1
            if l < r:
                nums[r], nums[l] = nums[l], nums[r]

        nums[left], nums[r] = nums[r], nums[left]

        quicksort(nums, left,   r-1)
        quicksort(nums,  r+1, right)
        return nums

def main():
    unsorted_list = [random.randint(0, 100) for _ in range(10)]
    print("Before Selection Sort\t: ", unsorted_list)
    quicksort(unsorted_list, 0, len(unsorted_list) - 1)
    print("After Selevtion Sort\t: ", quicksort(unsorted_list, 0, len(unsorted_list) - 1))

if __name__ == '__main__':
    main()