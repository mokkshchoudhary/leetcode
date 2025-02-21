class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0,n):
            if target == nums[i]:
                for j in range(n-1,i-1,-1):
                    if target == nums[j]:
                        return[i,j]
        if target not in nums:
            return(-1,-1)
