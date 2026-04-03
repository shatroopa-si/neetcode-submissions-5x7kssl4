class Solution:
    def isPalindrome(self, s: str) -> bool:
        begin, end = 0, len(s)-1
        while begin < end:
            if (s[begin].isalpha() or s[begin].isdigit()) and (s[end].isalpha() or s[end].isdigit()):
                if s[begin].lower() != s[end].lower():
                    return False
                begin += 1
                end -= 1
            elif not(s[begin].isalpha() or s[begin].isdigit()):
                begin += 1
            else:
                end -= 1
        return True