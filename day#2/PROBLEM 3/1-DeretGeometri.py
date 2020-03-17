def deretGeo(l) :
    mls = 0
    for i in range(len(l)-1) :
        if l[i+1] % l[i] != 0 :
            mls += 1

    if mls > 1 :
        return "False"
    else :
        return "True"

    return l
def getList(n) :
    ListIn = []    
    for i in range(n) :
        ListIn.append(int(input("Masukan list ke  %d : " % (i+1))))

    sres = deretGeo(ListIn)
    return sres

    

lenLst = int(input("Masukan Panjang List : "))

hasil = getList(lenLst)
print("Output : {0}".format(hasil))