class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for st in strs:
            fmap = tuple(self.getFrequencyMap(st))
            if fmap in groups:
                groups[fmap].append(st)
            else:
                groups[fmap] = [st]
        return list(groups.values())
    

    def getFrequencyMap(self, string):
        fmap = [0] * 26
        for ch in string:
            fmap[ord(ch) - ord('a')] += 1
        return fmap
    
    
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
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
    
    def getFrequencyMap(self, string):
        fmap = [0] * 26
        for ch in string:
            fmap[ord(ch) - ord('a')] += 1
        return fmap