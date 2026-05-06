class Solution:
    delimiter = "|"
    def encode(self, strs: List[str]) -> str:
        """
            This function generates an encoded string for a list of strings.

            @param strs                 [List] of strings

            @returnValue encoded_str    [str] Encoded string
        """
        
        encoded_str = self.delimiter
        for s in strs:
            len_s = len(s)
            encoded_str += str(len_s) + self.delimiter + s + self.delimiter

        return encoded_str


    def decode(self, s: str) -> List[str]:
        """
            This function decodes the string to generate the original list of strings.

            @param s                    [str] Encoded string

            @returnValue decoded_strs   [list] Original list of strings
        """

        decoded_strs = []
        i = 0
        while i < len(s):
            # Fetch length of string
            len_s = ""
            if s[i] == self.delimiter:
                i += 1
                while i < len(s) and s[i] != self.delimiter:
                    len_s += s[i]
                    i += 1
            if len_s != "":
                len_s = int(len_s)
                i += 1          # skip next delimiter

                # Fetch string
                decoded_strs.append(s[i: i + len_s])
                i = i + len_s
            else:
                i += 1

        return decoded_strs
