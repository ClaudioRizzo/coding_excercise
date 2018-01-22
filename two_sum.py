class Solution:
    
    def get_original_index(self, n1, n2, nums):
        indexes = []
        for i in range(len(nums)):
            n = nums[i]
            if n==n1:
                indexes.append(i)
            elif n==n2:
                indexes.append(i)
            if len(indexes) == 2:
                break
       
        return indexes
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        snums = sorted(nums)
        
        r = len(snums) - 1 # last index
        l = 0
        
        while l < r:
            if snums[l] + snums[r] == target:
                # get the index in the original array
                return self.get_original_indexes(snums[l], snums[r], nums)
            elif snums[r] > target:
                r-=1
            elif snums[l] + snums[r] < target:
                l+=1
            print("l: %d, r: %d" % (l, r))

if __name__ == '__main__': 
    solution = Solution()
    solution.twoSum([2,6,7,15], 9)