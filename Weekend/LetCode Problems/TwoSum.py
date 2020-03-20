res = []
# nums = [3,2,4]
# target = 6
nums = [2,7,11,15]
target = 9

for i in range(len(nums)-1) :
    j = i + 1
    for j in range(j,len(nums)) :
        if nums[i] + nums[j] == target :
            res.extend([i, j])
print(res)