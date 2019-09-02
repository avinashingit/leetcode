from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        l = len(nums)
        for i in range(l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, l-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < l and nums[j] == nums[j-1]:
                        j += 1
                    while k > 0 and nums[k+1] == nums[k]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return result
