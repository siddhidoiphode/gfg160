class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=len(needle)
        h=len(haystack)
        s=0
        while s<h:
            if haystack[s:s+l]==needle :
                return s
            else:
                s+=1

        return -1
            
