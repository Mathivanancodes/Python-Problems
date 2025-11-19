class Solution(object):
    def findFinalValue(self, nums, original):
        d = 0
        for x in nums:
            if x % original == 0:
                bit = x // original
                if not(bit & (bit - 1)): d |= bit

        d = (d + 1) & ~d
        
        return original * d