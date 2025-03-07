class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        zero_id = 0
        for non_zero in range(0,n):
            if nums[non_zero] != 0:
                nums[zero_id] = nums[non_zero]
                zero_id +=1
        for i in range(zero_id,n):
            nums[i] = 0  
