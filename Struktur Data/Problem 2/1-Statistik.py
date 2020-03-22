def minimal(lists) :
    res = []
    for ls in lists :
        for i in range(len(ls)) :
            for j in range(i+1, len(ls)) :
                if ls[i] > ls[j] :
                    temp = ls[i]    
                    ls[i] = ls[j] 
                    ls[j] = temp
        res.append(str(ls[0]))
    return res

def maximal(lists) :
    res = []
    for ls in lists :
        for i in range(len(ls)) :
            for j in range(i+1, len(ls)) :
                if ls[i] < ls[j] :
                    temp = ls[i]    
                    ls[i] = ls[j] 
                    ls[j] = temp
        res.append(str(ls[0]))
    return res

def generateMinMax(lists) :
    if lists[0] == 'min' :
        hasil = minimal([lists[1], lists[2]])
        res = ' '
        result = res.join(hasil)
        return result
    elif lists[0] == 'max' :
        hasil = maximal([lists[1], lists[2]])
        res = ' '
        return res.join(hasil)
    else :
        return "Only min max accepted"

print('generateMinMax(["max", [1,3,5,2,7,1],[7,3,9,2,2]]) : # ' + generateMinMax(["max", [1,3,5,2,7,1],[7,3,9,2,2]]))
print('generateMinMax(["min", [1,3,5,2,7,1],[7,3,9,2,2]]) : # ' + generateMinMax(["min", [1,3,5,2,7,1],[7,3,9,2,2]]))