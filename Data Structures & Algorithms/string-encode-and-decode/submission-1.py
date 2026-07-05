class Solution:

    def encode(self, strs: List[str]) -> str:
        # t = []
        s = ""
        for i in strs:
            for j in i:
                s += str(ord(j))
                s += ":"
            s += ";"
        return s
    def decode(self, s: str) -> List[str]:
        t = []
        l = s.split(";")
        for k in range(len(l)-1):
            m = ""
            w = ""
            for j in l[k]:
                if j != ":":
                    m += j
                else:
                    w += chr(int(m))
                    m = ""
            t.append(w)
        return t



