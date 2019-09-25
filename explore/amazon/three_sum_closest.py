class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        diff = float('inf')
        l = len(nums)
        closest = None
        for i in range(l):
            j, k = i+1, len(nums)-1
            while j < k:
                d = abs(nums[i] + nums[j] + nums[k] - target)
                if d <= diff:
                    diff = d
                    closest = nums[i] + nums[j] + nums[k]
                if nums[i] + nums[j] + nums[k] == target:
                    diff = 0
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return closest
        
