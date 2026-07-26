class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        ans = []
        while i <= j:
            mid = (i +j)//2 
            if nums[mid] == target:
                ans.append(mid)
                break
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        
        return ans[-1] if ans else -1