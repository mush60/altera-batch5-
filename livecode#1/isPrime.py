def isPrime(number) :
	if number >= 2 :
		for i in range(2, number) :
			if number % i == 0 :
				return False
				break
		return True
	else :
		return False

def fullPrime(number) :
	new_num = number
	temp = []
	while new_num > 0 :
		stn = new_num % 10
		if isPrime(stn) == False :
			return "TIDAK"
		new_num = new_num//10
	return "YA"

	# count = 0
	# for i in temp :
	# 	if isPrime(i) == True :
	# 		count += 1
	# if count == len(temp) :
	# 	return "YA"
	# else :
	# 	return "TIDAK"

print(fullPrime(2))
print(fullPrime(9))
print(fullPrime(3))
print(fullPrime(231))
print(fullPrime(33))


