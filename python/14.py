class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        matched = strs[0]
        for string in strs[1:]:
            temp = ""
            while matched and string:
                if matched[0] == string[0]:
                    temp += matched[0]
                else:
                    break
                matched = matched[1:]
                string = string[1:]
            matched = temp
        return matched
        
