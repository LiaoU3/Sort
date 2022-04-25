import random
def quick_sort(nums):
    return _sort(nums, 0, len(nums) - 1)

def _sort(nums, left, right):
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

        _sort(nums, left,   r-1)
        _sort(nums,  r+1, right)
        return nums

def main():
    unsorted_list = [random.randint(0, 100) for _ in range(10)]
    print("Before Selection Sort\t: ", unsorted_list)
    quick_sort(unsorted_list)
    print("After Selevtion Sort\t: ", quick_sort(unsorted_list))

if __name__ == '__main__':
    main()