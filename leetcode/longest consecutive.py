class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        longestConsecutive = 1
        currentConsecutive = 1

        for i in range(len(nums) - 1):
            if (nums[i]+1 == nums[i+1]):
                currentConsecutive+=1
            elif nums[i] == nums[i+1]:
                continue
            else:
                if currentConsecutive > longestConsecutive:
                    longestConsecutive = currentConsecutive
                currentConsecutive = 1
        if currentConsecutive > longestConsecutive:
            longestConsecutive = currentConsecutive
        
        return longestConsecutive
