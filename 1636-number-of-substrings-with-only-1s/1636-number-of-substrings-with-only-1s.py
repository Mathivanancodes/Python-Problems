class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        lyst = s.split("0")
        cnt = 0
        for i in lyst:
            cnt += len(i)*(len(i)+1)//2
        return cnt %(10**9+7)