def twoSum(nums, target):
    res = {}
    for i in range(len(nums)):
        if target - nums[i] in res:
            return [res[target - nums[i]], i ]
        else:
            res[nums[i]] = i

print(twoSum([2, 7, 11, 15],9))