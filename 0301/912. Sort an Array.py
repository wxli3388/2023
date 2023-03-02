class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return nums
        half = len(nums)//2
        left = self.sortArray(nums[:half])
        right = self.sortArray(nums[half:])
        i, j = 0, 0
        temp = []
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                temp.append(left[i])
                i+=1
            elif left[i]>right[j]:
                temp.append(right[j])
                j+=1
        while i<len(left):
            temp.append(left[i])
            i+=1
        while j<len(right):
            temp.append(right[j])
            j+=1
        return temp
                