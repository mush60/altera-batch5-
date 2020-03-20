def kelopokArray(numbers) :
    result = [[],[],[]]
    for i in range(len(numbers)) :
        if numbers[i] % 3 == 0 :
            result[2].append(numbers[i])
        else :
            if numbers[i] % 2 == 0 :
                result[0].append(numbers[i])
            else :
                result[1].append(numbers[i])

    return result

print(kelopokArray([2, 4, 6]))
print(kelopokArray([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(kelopokArray([100, 151, 122, 99, 111]))
print(kelopokArray([]))