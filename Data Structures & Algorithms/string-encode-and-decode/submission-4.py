class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return " "

        s= "\n".join(strs)
        return s 

    def decode(self, s: str) -> List[str]:
        if s == " ":
            return []
        strs = s.split('\n')
        return strs
