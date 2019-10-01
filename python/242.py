class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S, T = [0] * 26, [0]*26
        for c in s:
            S[ord(c)-97] += 1
        for c in t:
            T[ord(c)-97] += 1
        return S == T
