class Solution:

    def encode(self, strs: List[str]) -> str:
        return '|'.join(strs) + '|' + str(len(strs)) if len(strs) > 0 else ''
    def decode(self, s: str) -> List[str]:
        return s.split('|')[: -1] if len(s) > 0 else []