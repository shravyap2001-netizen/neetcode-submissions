class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zc = 0
        d = [0]
        for i in nums:
            if i == 0:
                zc += 1
            else:
                p *= i
        # if len(nums) - zc < 2 and (nums[0] == 0):
        #     return d * len(nums)
        # elif len(nums) - zc > 2 and (nums[-1] == 0):
        #     return d * len(nums)
        if zc > 1 and len(nums) > 1:
            return d * len(nums)
        else:
            output = []
            for j in nums:
                if zc:
                    if j != 0:
                        output.append(0)
                    else:
                    # r = p//j
                        output.append(p)
                else:
                    output.append(p//j)
        return output
        

        