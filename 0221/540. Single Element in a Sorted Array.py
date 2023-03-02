class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            mid = left+(right-left)//2
            even = mid%2==0
            if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
                return nums[mid]
            if even and nums[mid]==nums[mid+1] or not even and nums[mid]==nums[mid-1]:
                left = mid+1
            else:
                right = mid-1
        return nums[left]
