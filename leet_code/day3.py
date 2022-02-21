#Two Sum
class Solution:
    def twoSum(self, nums,target):
        processed_number_dict = dict()
        for a in range(len(nums)):
            if (target-nums[a]) in processed_number_dict.keys():
                return([a, processed_number_dict[target-nums[a]]])
            else:
                processed_number_dict[nums[a]] = a


# Number of Islands
