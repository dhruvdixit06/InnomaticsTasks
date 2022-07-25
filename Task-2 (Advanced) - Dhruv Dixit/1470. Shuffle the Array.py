class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        for i in range(0,n):
            x=nums[i]
            y=nums[i+n]
            res.append(x)
            res.append(y)
        return res