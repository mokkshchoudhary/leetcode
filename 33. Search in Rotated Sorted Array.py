class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range (0,n):
            if target == nums[i]:
                return (i)
        if target not in nums:
                return (-1)       
