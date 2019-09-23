class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = map(int, version1.split("."))
        version2 = map(int, version2.split("."))
        for i in range(max(len(version1), len(version2))):
            one = version1[i] if i < len(version1) else 0
            two = version2[i] if i < len(version2) else 0
            if one < two:
                return -1
            elif one > two:
                return 1
        return 0
