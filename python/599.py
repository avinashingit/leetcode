from collections import defaultdict


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index = defaultdict(int)
        for i, rest in enumerate(list1):
            index[rest] = i

        min_val = float("inf")
        result = []

        for j, rest in enumerate(list2):
            if rest in index:
                total = index[rest] + j
                if total == min_val:
                    result.append(rest)
                elif total < min_val:
                    result = [rest]
                    min_val = total
        return result
