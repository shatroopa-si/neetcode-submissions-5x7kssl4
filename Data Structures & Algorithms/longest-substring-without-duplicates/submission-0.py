class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s)==0:
            return 0
        begin, max_l = 0, 1
        ch_map = {}             # {ch: index of ch in s}
        for i in range(len(s)):
            ch = s[i]
            if (ch not in ch_map) or            \
                (ch in ch_map and begin > ch_map[ch]):
                max_l = max(max_l, i-begin+1)
            else:
                begin = ch_map[ch] + 1
            ch_map[ch] = i
        return max_l
