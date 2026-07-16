class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        for i in range(len(temperatures)):
            a = i +1
            while a < len(temperatures):
                    if temperatures[i] < temperatures[a]:
                        st.append(a-i)
                        break
                    else:
                        a += 1
            else:
                st.append(0)
        return st   