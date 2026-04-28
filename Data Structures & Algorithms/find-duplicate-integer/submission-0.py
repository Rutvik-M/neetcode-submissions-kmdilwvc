class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 0
        
        # Outer loop: The Anchor
        while left < len(nums):
            
            # Reset the scanner to the very end of the array for a fresh sweep
            right = len(nums) - 1
            
            # Inner loop: The Scanner
            # Keep shrinking right until it bumps into left
            while left < right:
                if nums[left] == nums[right]:
                    return nums[left]
                else:
                    right -= 1
                    
            # The sweep finished with no match. Move the anchor forward!
            left += 1