class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Make into alphanumeric string
        s_an = ""
        for ch in s:
            s_an += ch.lower() if ch.isalnum() else ""
        print(s_an)

        # Check for palindrome
        i = 0 
        while i < len(s_an) // 2:
            if s_an[i] != s_an[-1-i]:
                return False
            i += 1
        return True

        