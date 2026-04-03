class Solution:
    def isPalindrome(self, s: str) -> bool:
        begin, end = 0, len(s)-1
        while begin < end:
            if s[begin].isalnum() and s[end].isalnum():
                if s[begin].lower() != s[end].lower():
                    return False
                begin += 1
                end -= 1
            elif not s[begin].isalnum():
                begin += 1
            else:
                end -= 1
        return True