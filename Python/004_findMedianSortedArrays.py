def findMedianSortedArrays(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    n = len(nums)
    h = int((n/2) - 0.5)
    if n % 2 != 0:
        return float(nums[(h)])
    else:
        return (nums[h] + nums[h + 1])/2