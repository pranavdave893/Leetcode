from collections import Counter
class Solution(object):
    def sortColors(self, nums):
        count = Counter(nums)
        value_count = 0
        ans = 0
        for key, val in sorted(count.items(), key=lambda x:-x[1]):
            value_count += val
            ans += 1
            if value_count >= len(nums) // 2:
                return ans


abc = Solution()
print (abc.sortColors([1,2,3,4,5,6,7,8,9,10]))
