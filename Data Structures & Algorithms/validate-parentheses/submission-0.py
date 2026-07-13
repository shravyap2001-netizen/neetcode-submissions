class Solution:
    def isValid(self, s: str) -> bool:
        d = {"]":"[","}":"{",")":"("}
        st = []
        for i in s:
            if i not in d:
                st.append(i)
            else:
                if len(st)!= 0:
                    if st[-1] == d[i]:
                        st.pop()
                    else:
                        return False
                else:
                    return False
        else:
            return True if len(st) == 0 else False