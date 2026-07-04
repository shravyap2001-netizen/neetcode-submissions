class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        output = []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        output = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return [output[j][0] for j in range(k)]
