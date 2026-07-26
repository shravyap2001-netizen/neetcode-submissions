class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        i = 1
        j = len(numbers)
        
        ans = []
        while i < j:
            s = numbers[i-1] + numbers[j-1]
            if s == target:
                ans.append(i)
                ans.append(j)
                break
            elif s < target:
                i += 1
            else:
                j -= 1
        return ans
        

                

