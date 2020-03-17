def deretTerdekat(l) :
    lx = []
    lo = []
    lj = []
    # cari titik lokasi x dan o :
    for i in range(len(l)) :
        if l[i] == 'x' :
            lx.append(i+1)
        elif l[i] == 'o' :
            lo.append(i+1)
    for j in range(len(lx)) :
        for k in range(len(lo)) :
            if lx[j] > lo[k] :
                lj.append(abs(lo[k] - lx[j]))
            else :
                lj.append(abs(lx[j] - lo[k]))
            
    if len(lx) == 0 or len(lo) == 0 :
        return 0
    else :
        return min(lj)
    # return [lx, lo, min(lj)]


def getList(n) :
    ListIn = []    
    for i in range(n) :
        ListIn.append(input("Masukan list ke  %d : " % (i+1)))

    sres = deretTerdekat(ListIn)
    return sres

lenLst = int(input("Masukan Panjang List : "))

hasil = getList(lenLst)
print("Output : {0}".format(hasil))