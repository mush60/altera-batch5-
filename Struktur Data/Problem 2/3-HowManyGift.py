def howManyGift(maxBudget, gifts) :
    total = 0
    # sorting gifts
    for i in range(len(gifts)) :
        for j in range(len(gifts)) :
            if gifts[i] < gifts[j] :
                temp = gifts[i]
                gifts[i] = gifts[j]
                gifts[j] = temp
    for i in range(len(gifts)) :
        for j in range(i, len(gifts)) :
            if maxBudget - sum(gifts[i:j]) > -1 :
                len_gifts = len(gifts[i:j])
                if total == 0 :
                    total += len_gifts
                else :
                    if total < len_gifts :
                        total = len_gifts
            # print(gifts)
            # print(sum(gifts[i:j]), len(gifts[i:j]), total, gifts[i:j])
    return total
            
print(howManyGift(30000,[15000,12000,5000,3000,10000]))
print(howManyGift(10000,[2000,2000,3000,1000,2000,10000]))
print(howManyGift(0,[10000,3000]))
# howManyGift(30000,[15000,12000,5000,3000,10000])