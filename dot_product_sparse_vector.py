class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse = [(i, v) for i, v in enumerate(nums) if v]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        
        i1 = 0
        i2 = 0         
        while i1 < len(vec.sparse) and i2 < len(self.sparse):
            if vec.sparse[i1][0] < self.sparse[i2][0]:
                i1 += 1
            elif vec.sparse[i1][0] > self.sparse[i2][0]:
                i2 += 1
            else:
                product += vec.sparse[i1][1] * self.sparse[i2][1]
                i1 += 1
                i2 += 1
                
        return product

v1 = Solution([1,0,0,0,2,3])
v2 = Solution([0,3,0,4,0])