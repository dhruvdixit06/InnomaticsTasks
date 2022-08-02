class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t=set(nums)
        for i in t:
            if nums.count(i)==1:
                return i