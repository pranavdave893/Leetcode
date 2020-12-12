class Solution(object):
    # O(N)
    def find_missing_number(self, nums, k):
        
        prev = nums[0]

        for curr in nums[1:]:
            diff = curr - prev - 1

            if k <= diff:
                break

            prev = curr
            k -= diff
        
        print(prev + k)


abc = Solution()
abc.find_missing_number([4,7,8,9,10], 4)