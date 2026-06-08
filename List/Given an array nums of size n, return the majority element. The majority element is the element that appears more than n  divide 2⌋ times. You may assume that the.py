nums=[1,1,2,2,2,3,3]
for i in nums:
    if nums.count(i)>len(nums)/2:
        print(i)
        break
