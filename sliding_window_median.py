from bisect import bisect, insort
class SolutionSortedArrayFast(object):
    def medianSlidingWindow(self, nums, k):
        win, rv = nums[:k], []
        win.sort()
        odd = k%2
        for i,n in enumerate(nums[k:],k):
            rv.append((win[k//2]+win[k//2-1])//2. if not odd else win[(k-1)//2])
            win.pop(bisect(win, nums[i-k]) -1 ) # <<< bisect is faster than .remove()
            insort(win, nums[i])
        rv.append((win[k//2]+win[k//2-1])//2. if not odd else win[(k-1)//2])
        return rv

abc = SolutionSortedArrayFast()
abc.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 4)

