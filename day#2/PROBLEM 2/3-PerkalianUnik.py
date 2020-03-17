def PerkalianUnik(lst) :
    strres = ''
    for i in range(len(lst)) :
        res = 1
        for j in range(len(lst)) :
            if(j != i) :
                res = res * lst[j]
        strres = strres + str(res) + " "

    return strres

def getList(n) :
    ListIn = []    
    for i in range(n) :
        ListIn.append(int(input("Masukan list ke  %d : " % (i+1))))

    sres = PerkalianUnik(ListIn)
    return sres

    

lenIn = int(input("Masukan Panjang List : "))

hasil = getList(lenIn)

print("Output : {0}".format(hasil))

