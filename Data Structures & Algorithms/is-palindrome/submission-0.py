class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remomve all invalid characters
        refined_str = self.getRefinedString(s)

        # Check palindrome
        begin, end = 0, len(refined_str)-1
        while begin < end:
            if refined_str[begin] != refined_str[end]:
                return False
            begin += 1
            end -= 1
        return True

    def getRefinedString(self, s: str) -> str:
        refined_str = ""
        for ch in s:
            if ch.isalpha():
                refined_str += ch.lower()
            elif ch.isdigit():
                refined_str += ch
        return refined_str
