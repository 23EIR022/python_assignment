class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=set() #create a set to avoid duplicates
        nums.sort() #sort the num

        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k: 
                ans=nums[i]+nums[k]+nums[j] 
                if ans<0: 
                    j+=1
                elif ans>0: 
                    k-=1
                else:
                    l.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
        return list(l)
