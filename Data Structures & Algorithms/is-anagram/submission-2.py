class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams should have same length
        if len(s) == len(t):
            # Delete every character 1 by 1 in t which is both in s & t
            for ch in s:
                t = t.replace(ch, '', 1) if ch in t else t
            
            # Check if t still has chars left
            if len(t) == 0:
                return True
        return False
        
