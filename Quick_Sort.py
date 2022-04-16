class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, left, right):
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

            self.quicksort(nums, left,   r-1)
            self.quicksort(nums,  r+1, right)

def main():
    solution = Solution()
    nums = [5,2,3,1]
    solution.quicksort(nums, 0, len(nums) - 1)
    print(nums)

if __name__ == '__main__':
    main()