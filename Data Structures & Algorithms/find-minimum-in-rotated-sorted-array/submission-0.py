class Solution:
    def findMin(self, nums: List[int]) -> int:

        min_value = -1000

        low = 0
        high = len(nums)-1

        while low<high:
            mid = (low+high)//2

            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid

            if nums[mid] < min_value:
                min_value = nums
        return nums[low]