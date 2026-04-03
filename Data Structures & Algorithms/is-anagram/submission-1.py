class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for ch in s:
                if ch in t:
                    t = t.replace(ch, '', 1)
            if len(t) == 0:
                return True
            else: 
                return False
        else: 
            return False