from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        ans = []
        
        for sp in spells:
            left, right = 0, m - 1
            index = -1
            
            while left <= right:
                mid = (left + right) // 2
                if sp * potions[mid] >= success:
                    index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            ans.append(0 if index == -1 else m - index)
        
        return ans