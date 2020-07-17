def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """  
  n,j = len(nums),0
  newlist = []
  for i in range(0,len(nums)):
      if(nums[i] != val):
          nums[j] = nums[i]
          j = j + 1
          
          #newlist.append(nums[i])
  return j
  #nums.remove(val)
  #return len(nums)
  # i = 0
  # print(len(nums))
  #print(nums[len(nums) - 1])
  #while(i<=(len(nums) - 1)):
  #for i in range(0,len(nums)-1):
   #   if(nums[i] == val):
    #      print (nums)
          #del nums[i]
          #nums.pop(i)
          #nums.remove(val)
         # print(nums)
     # i+=1
          
  #print(nums)