class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        if len(strs) == 1:
            return [strs]
        for st in strs:
            checked = False
            for group in groups:
                if self.chkAnagram(st, group[0]):
                    group.append(st)
                    checked = True
            else:
                if not checked: 
                    groups.append([st])
        return groups
            

    def chkAnagram(self, s, t):
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