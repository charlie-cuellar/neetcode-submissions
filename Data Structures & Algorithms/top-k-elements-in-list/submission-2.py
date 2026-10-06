class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        mahp = {}
        for num in nums:
            if num not in mahp:
                mahp[num] = 0
            mahp[num] += 1
        # print(mahp)
        smahp = dict(sorted(mahp.items(), key=lambda item: item[1], reverse=True))
        # print(smahp)
        lst = list(smahp.keys())
        # print(lst)
        for i in range(k):
            ans.append(lst[i])
        return ans
