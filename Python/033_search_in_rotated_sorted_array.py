def search(nums: List[int], target: int) -> int:
    def find_middle(arr, low, high):
        if high < low: 
            return -1
        if high == low: 
            return low 

        mid = (low + high)//2

        if mid < high and arr[mid] > arr[mid + 1]: 
            return mid 
        if mid > low and arr[mid] < arr[mid - 1]: 
            return (mid-1) 
        if arr[low] >= arr[mid]: 
            return find_middle(arr, low, mid-1) 
        return find_middle(arr, mid + 1, high) 
    def binary_search(arr, low, high, target):
        if high < low: 
            return -1     
        mid = (low + high)//2

        if target == arr[mid]: 
            return mid 
        if target > arr[mid]: 
            return binary_search(arr, (mid + 1), high,target); 
        return binary_search(arr, low, (mid -1), target)

    
    middle = find_middle(nums, 0, len(nums)-1)
    if middle == -1: 
        return binary_search(nums, 0, len(nums)-1, target) 


    if nums[middle] == target: 
        return middle
    if nums[0] <= target: 
        return binary_search(nums, 0, middle-1, target)
    return binary_search(nums, middle+1, len(nums)-1, target)