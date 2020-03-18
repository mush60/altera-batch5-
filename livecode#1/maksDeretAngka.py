def maksDeretBilangan(numbers):
    list_res = []
    count = 0
    for i in range(len(numbers)) :
    	ldr = i+1
    	while ldr <= len(numbers) :
    		# print("%d : %d " % (i, ldr))
    		list_res.append(sum(numbers[i:ldr]))
    		ldr += 1   	
    return max(list_res)

print(maksDeretBilangan([-2, -1, -3, 4, -1, 2, 1, -5, 4]))
print(maksDeretBilangan([-2, -5, 6, -2, -3, 1, 5, -6]))