import random
def merge_sort(nums:list)->list:
    if len(nums) <= 1:
        return nums
    left  = merge_sort(nums[ :len(nums)//2])
    right = merge_sort(nums[len(nums)//2 :])
    point_left  = 0
    point_right = 0
    sorted_nums = []
    while point_left < len(left) and point_right < len(right):
        if left[point_left] < right[point_right]:
            sorted_nums.append(left[point_left])
            point_left += 1
        else:
            sorted_nums.append(right[point_right])
            point_right += 1
    if point_left == len(left):
        sorted_nums += right[point_right:]
    elif point_right == len(right):
        sorted_nums += left[point_left:]
    return sorted_nums

def main():
    unsorted_list = [random.randint(0, 100) for _ in range(10)]
    # unsorted_list = [12, 11, 13, 5, 6, 7]
    print("Before Selection Sort\t: ", unsorted_list)
    print("After Selevtion Sort\t: ", merge_sort(unsorted_list))

if __name__ =="__main__":
    main()