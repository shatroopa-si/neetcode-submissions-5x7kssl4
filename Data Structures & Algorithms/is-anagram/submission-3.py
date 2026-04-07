class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            Since, it is assumed that input strings contain only lower case chars from the english alphabet,
            the space complexity is: O(1)
        """
        # Anagrams should have same length
        if len(s) == len(t):
            # Create hashmaps for both s & t; counting the frequency of chars in each string
            s_map, t_map = {}, {}
            for ch in s:
                s_map[ch] = s_map.get(ch, 0) + 1
            for ch in t:
                t_map[ch] = t_map.get(ch, 0) + 1
            
            # Check if t still has chars left
            if s_map == t_map:
                return True
        return False


    def isAnagramQuad(self, s: str, t: str) -> bool:
        """
            The character replace function works in linear time.
            So, this function runs in quadratic time.
        """
        # Anagrams should have same length
        if len(s) == len(t):
            # Delete every character 1 by 1 in t which is both in s & t
            for ch in s:
                t = t.replace(ch, '', 1) if ch in t else t
            
            # Check if t still has chars left
            if len(t) == 0:
                return True
        return False
        
