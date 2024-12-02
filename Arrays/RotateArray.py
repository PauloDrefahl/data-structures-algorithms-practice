class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums) # ignore rotations that are larger than the length of nums
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k] # here we grab the number of rotations use the - sign to place them in the front and do the same in the back 
        
        
            