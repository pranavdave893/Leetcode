from numpy import median

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_x = len(nums1)
        len_y = len(nums2)

        if len_x < len_y:
            min_len_num = nums1
            max_len_num = nums2
        else:
            min_len_num = nums2
            max_len_num = nums1
        
        partition_size_min = len(min_len_num) / 2
        
        while True:
            partition_size_max = ((len_x + len_y + 1) / 2) - partition_size_min

            min_partition_last = float('-inf')
            max_partition_last = float('-inf')

            min_partition_first = float('inf')
            max_partition_first = float('inf')

            if min_len_num[0:partition_size_min]:
                min_partition_last = min_len_num[:partition_size_min][-1]
            
            if max_len_num[partition_size_max:]:
                max_partition_first = max_len_num[partition_size_max:][0]
            
            if max_len_num[:partition_size_max]:
                max_partition_last = max_len_num[:partition_size_max][-1]
            
            if min_len_num[partition_size_min:]:
                min_partition_first = min_len_num[partition_size_min:][0]

            if min_partition_last <= max_partition_first and max_partition_last <= min_partition_first:

                if (len_x + len_y) % 2 == 0:
                    avg = median([max(min_partition_last, max_partition_last), min(min_partition_first, max_partition_first)])
                    
                else:
                    avg = max(min_partition_last, max_partition_last)
                
                return avg
            
            elif(max_len_num[:partition_size_max][-1] > min_len_num[partition_size_min:][0]):
                partition_size_min += 1
            
            else:
                partition_size_min -= 1

abc = Solution()
print (abc.findMedianSortedArrays([23,26,31,35], [3,5,7,9,11,16]))
