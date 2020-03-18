def checkDigit(n) :
    new_number = n
    temp = 0
    list_number = []
    while new_number > 0 :
        satuan = new_number % 10
        list_number.append(satuan)
        new_number = new_number//10

    count = 0
    list_prime = [2, 3, 5, 7]
    for i in range(len(list_number)) :
    	for j in list_prime :
    		if list_number[i] == j :
    			count += 1
    		else :
    			count += 0
    		# print('%d : %d' % (list_number[i], j))


    if count == len(list_number) :
    	return 'YA'
    else :
    	return 'TIDAK'


        
def fullPrime(number):
    if number > 1 :
        count = 0
        for i in range(1, number) :
            if number % i == 0 :
                count += 1
            else :
                count += 0
        if count < 2 :
            return checkDigit(number)
            # print('YA')
        else :
            return 'TIDAK'
    else :
    	return 'TIDAK'

print(fullPrime(17))
print(fullPrime(23))
print(fullPrime(22))
print(fullPrime(59))