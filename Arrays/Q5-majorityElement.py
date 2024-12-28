#Question 5: we need tp just create a hasmap of the number of time that values appear. Then execite a max function with the key parameter to grab the key associated with that
#Largest value. 

class Solution(object):
    def majorityElement(self, nums):
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        return max(count, key=count.get)
        

print(Solution().majorityElement([3,2,3])) #3