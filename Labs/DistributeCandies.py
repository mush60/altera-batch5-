def distCandy(candies) :
    res = []
    for i in candies :
        if i not in res :
            res.append(i)
    if len(res) < len(candies)//2 :
        return len(res)
    else :
        return len(candies)//2
            

# cand = [1,1,2,2,3,3]
cand = [1,1,2,3,3,4,5]
print(distCandy(cand))