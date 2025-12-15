class Solution:
    def getDescentPeriods(self, prices):
        ans = 0
        cnt = 1

        for i in range(len(prices)):
            if i == 0:
                ans += cnt
                continue

            if prices[i] == prices[i - 1] - 1:
                cnt += 1
            else:
                cnt = 1

            ans += cnt

        return ans