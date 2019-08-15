# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution:

    def calculateMaximumDepth(self, nesteList):
        depth = 1
        for l in nesteList:
            if not l.isInteger():
                depth = max(depth, 1+self.calculateMaximumDepth(l.getList()))
        return depth

    def dfs(self, nestedList, depth):
        total = 0
        for l in nestedList:
            if l.isInteger():
                total += depth*l.getInteger()
            else:
                total += self.dfs(l.getList(), depth - 1)
        return total

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        maxdepth = self.calculateMaximumDepth(nestedList)
        return self.dfs(nestedList, maxdepth)

# Another Method


class Solution2:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        total_sum, curr_sum = 0, 0
        while len(nestedList):
            newList = []
            for l in nestedList:
                if l.isInteger():
                    curr_sum += l.getInteger()
                else:
                    for ls in l.getList():
                        newList.append(ls)
            total_sum += curr_sum
            nestedList = newList
        return total_sum
