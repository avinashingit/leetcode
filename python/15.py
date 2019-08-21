from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resultset = set()
        nums.sort()
        result = []
        l = len(nums)
        for i in range(l-2):
            j, k = i+1, l-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if tuple([nums[i], nums[j], nums[k]]) not in resultset:
                        result.append([nums[i], nums[j], nums[k]])
                        resultset.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return result
