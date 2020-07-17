def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    n = len(nums)
    for i in range(0,n):
        
        if(nums[i] == target):
            return i
        elif(nums[i] > target):
            return i
        elif(i == (n - 1)):
            return n