# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


from typing import List


nums = [2,7,11,5]
target = 9


nums1 = [2,3,8,6,5,11,9]
target1 = 9

# return indices of the two numbers [x, y] 
# lets consider two variable 
# x = 2, y = 7 , 
# x + y = target however we don't need to check previous combinations [0 ,1] == [1, 0] 
# So instead brute forcing the all the combination O(n^2) we can use hash map to optimize solution time by 
# y = target - x basically it ignores the swapped value combination.

def two_sum(nums:list[int], target:int) -> List[int]:
    d = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in d:
            return [d[difference], i]
        else:
            d[nums[i]] =  i

print(two_sum(nums, target))
print(two_sum(nums1, target1))


