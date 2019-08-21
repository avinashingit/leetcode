from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return [key for key, value in counts.items() if value == 1][0]
