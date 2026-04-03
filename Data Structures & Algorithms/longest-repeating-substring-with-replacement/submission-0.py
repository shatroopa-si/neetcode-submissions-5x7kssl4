class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s is None or len(s)<1:
            return 0
        
        
        begin, max_l, n = 0, 1, len(s)
        ch_freq_map = {s[0]: 1}                # Map of chars and their frequencies in the substring
        most_frequent_ch = s[0]
        for i in range(1, n):
            ch = s[i]
            ch_freq_map[ch] = ch_freq_map[ch] + 1 if ch in ch_freq_map else 1
            most_frequent_ch = most_frequent_ch if ch_freq_map[most_frequent_ch] > ch_freq_map[ch] else ch
            if (i - begin + 1) - ch_freq_map[most_frequent_ch] > k:
                ch_freq_map[s[begin]] -= 1
                begin += 1
            max_l = max(i - begin + 1, max_l)            

        return max_l