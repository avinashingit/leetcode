class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            maxsum = max(maxsum, nums[i])
        return maxsum
