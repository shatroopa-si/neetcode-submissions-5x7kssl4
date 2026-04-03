class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        ch_map_t = {c: t.count(c) for c in t}
        ch_map_s = {c: s.count(c) for c in s}
        if ch_map_t == ch_map_s:
            return s


        begin, min_len = 0, len(s)
        ch_map_s = {}
        min_str = ""
        indices, j = [], 0
        for i in range(len(s)):
            if s[i] in ch_map_t:
                ch_map_s[s[i]] = ch_map_s.get(s[i], 0) + 1
                indices.append(i)
                begin = indices[j]
                
                while s[begin] in ch_map_t and ch_map_s[s[begin]] > ch_map_t[s[begin]]:
                    ch_map_s[s[begin]] -= 1
                    j += 1
                    begin = indices[j]
                
                if all([ch_map_t[ch] <= ch_map_s.get(ch, 0) for ch in ch_map_t]):
                    if min_len >= i - begin + 1:
                        min_len = i - begin + 1
                        min_str = s[begin: i+1]
        return min_str


