class Solution(object):
    def searchRange(self, nums, target):
        """
        Must run it in O(log n) time.
        """
        if not nums:
            return [-1,-1]
        def b_search(nums, target, left):
            lo, high = 0, len(nums)
            while (lo < high):
                mid = (lo + high) / 2

                if nums[mid] == target:
                    if left:
                        high = mid
                    else:
                        lo = mid + 1
                
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    high = mid
            
            return lo
        
        left = b_search(nums, target, True)
        right = b_search(nums, target, False)

        if 0<= left < len(nums) and nums[left] == target:
            return [left, right-1]
        else:
            return [-1,-1]
        # lo, high = 0 , len(nums)-1
        # self.answer = []
        # def recur(nums, target, lo, high):
        #     while high >= lo:
        #         # import pdb; pdb.set_trace()
        #         mid = lo + (high-lo) // 2

        #         if nums[mid] == target:
        #             start_position = recur(nums, target, lo, mid-1)
        #             if start_position == -1:
        #                 self.answer.append(mid)
        #             else:
        #                 self.answer.append(start_position)

        #             end_position = recur(nums, target, mid+1, high)
        #             if end_position == -1:
        #                 self.answer.append(mid)
        #             else:
        #                 self.answer.append(end_position)
                    
        #             break
                
        #         elif nums[mid] < target:
        #             lo = mid+1
                
        #         elif nums[mid] > target:
        #             high = mid-1
            
        #     return -1
        
        # recur(nums, target, lo, high)

        # print list(set(self.answer))

abc = Solution()
print (abc.searchRange([5,7,7,8,8,10], 8))