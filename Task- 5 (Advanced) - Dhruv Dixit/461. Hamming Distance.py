class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n=x^y
        n=bin(n)
        c=n.count("1")
        return c