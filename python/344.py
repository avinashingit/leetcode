class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        mid = int(l//2)
        for i in range(mid):
            s[i], s[l-i-1] = s[l-i-1], s[i]
        return s
