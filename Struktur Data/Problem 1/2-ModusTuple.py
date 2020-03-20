def cariModus(numbers) :
    list_numbers = []
    list_n = []
    list_nx = []
    for i in range(len(numbers)) :  
        list_numbers.append(numbers[i])
    
    for i in range(len(numbers)) :
        temp = list_numbers
        count = 0
        while numbers[i] in temp :
            count += 1
            temp.pop(temp.index(numbers[i]))
        if count != 0 :
            list_n.append(numbers[i])
            list_nx.append(count)
            

    if len(list_nx) <= 1 :
        return -1
    else :
        return list_n[list_nx.index(max(list_nx))]

print(cariModus((10, 4, 5, 2, 4)))
print(cariModus((5, 10, 10, 6, 5)))
print(cariModus((1, 1, 1, 1)))

