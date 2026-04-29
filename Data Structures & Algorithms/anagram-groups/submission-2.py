class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            Assume all chars are in small case.
        """
        group_ans = []
        # Input checks
        if len(strs) == 0:
            group_ans = strs
        
        elif len(strs) == 1:
            group_ans = [strs]
        
        else:
            # Compare anagrams of input strings using a hashmap of frequency of it's characters.
            group = {}
            for string in strs:
                string_cc = self.getHash(string)
                if string_cc in group:
                    group[string_cc].append(string)
                else:
                    group[string_cc] = [string]
            for g in group:
                group_ans.append(group[g])        
        return group_ans


    def getHash(self, s: str) -> Tuple:
        """
            This function returns a frequency array as a tuple for an input string.
            Assumption: all characters are lower case.

            @param s                [str] Input string

            @returnValue s_map      [Tuple] Frequency array
        """

        # Count frequency of characters
        s_map = [0]*26
        for ch in s:
            s_map[ord(ch)-ord('a')] += 1
        
        return tuple(s_map)