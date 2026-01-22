'''Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).'''
class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.j = 0
        
        while True:
            is_sorted = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    is_sorted = False
                    break
            
            if is_sorted or len(nums) < 2:
                break
            
            # Find leftmost minimum sum pair
            min_sum = float('inf')    #use instead of this min_sum= nums[0} + nums[1] As a initial value 
            target_idx = 0
            
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i+1]
                if s < min_sum:
                    min_sum = s
                    target_idx = i
            
        
            new_val = nums[target_idx] + nums[target_idx + 1]
            nums[target_idx : target_idx + 2] = [new_val]
            
            self.j += 1
            

        return self.j
