from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        contains = False
        n1, n2 = len(s1), len(s2)
        if n1 == n2:
            return set(s1)==set(s2)
        elif n1 > n2:
            return False
        else:
            if s1 in s2:            # Check if string is present as it is
                return True
            for i, c in enumerate(s2[: -n1+1]):
                if c in s1:
                    #print(c, Counter(smaller_str), Counter(larger_str[i:i+ns]))
                    contains = contains or Counter(s1) == Counter(s2[i:i+n1])
            return contains

        