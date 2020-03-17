def checkPrime(number):
    count = 0
    if number == 2 :
        count += 0
    elif number > 2 :
        for i in range(2, number) :
            if number % i == 0 :
                count += 1
            else :
                count += 0
    else :
        count += 1

    if count > 0 :
        return "TIDAK"
    else :
        return "YA"


print(checkPrime(2))
print(checkPrime(5))
print(checkPrime(7))
print(checkPrime(9))
print(checkPrime(15))