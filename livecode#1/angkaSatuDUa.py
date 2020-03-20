def angkaSatuDua(numbers) :
	print(numbers)
	ind1 = []
	ind2 = []
	for i in range(len(numbers)) :
		if numbers[i] == 1 : 
			ind1.append(i)
		elif numbers[i] == 2 :
			ind2.append(i)
		else :
			continue
	for j in range(len(ind1)) :
		onum = numbers[ind1[j]+1]
		numbers[ind1[j]+1] = 2
		numbers[ind2[j]] = onum


	print(ind1)
	print(ind2)
	print(numbers)



angkaSatuDua([6, 3, 5, 2, 1, 3, 6, 2, 1, 3])

