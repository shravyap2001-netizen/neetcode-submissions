class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # p = 1
        # for i in nums:
        #     if i != 0:
        #         p *= i
            
        # output = []
        # for j in nums:
        #     if j != 0 :
        #         r = p//j
        #     else:
        #         r =0
        #     output.append(r)
        # return output
        ans = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            ans.append(product)

        return ans
    

        