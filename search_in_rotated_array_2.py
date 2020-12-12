class Solution(object):
    def search(self, nums, target):

        l, r = 0, len(nums)-1

        while l<=r:

            mid = l + (r-l) // 2

            if nums[mid] == target:
                return True
            
            while l <= mid and nums[l] == nums[mid]:            # array = [8,8,8,8,8,8,7]
                l += 1
            
            if nums[l] <= nums[mid]:                            # [8,9,9,10,12,12,15,19]
                if nums[l] <= nums[target] < nums[mid]:         # target = 10
                    r = mid - 1
                else:
                    l = mid + 1                                 # target = 15
            
            else:                                               # [15,19,5,8,9,9,10,12,12]
                if nums[mid] < target <= nums[r]:               # target = 10
                    l = mid + 1
                else:                                           # target = 8
                    r = mid - 1
        
        return False