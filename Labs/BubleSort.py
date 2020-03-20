ls = [3, 1, 5, 5, 5, 2, 5, 2, 6, 87, 52]

for i in range(len(ls)) :
    for j in range(i+1, len(ls)) :
        if ls[i] > ls[j] :
            temp = ls[i]    
            ls[i] = ls[j] 
            ls[j] = temp

print(ls)

