class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        if strs == [""]:
            return ""
        if strs == []:
            return "xxx"
        for x in strs:
            s+=x+"\\xxx\\"
        print(s[:-5])
        return s[:-5]
    def decode(self, s: str) -> List[str]:
        if s=="xxx":
            return []
        if s == "":
            return [""]
        x=s.strip().split("\\xxx\\")
        return x