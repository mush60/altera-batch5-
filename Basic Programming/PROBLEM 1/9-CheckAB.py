def checkAB(mstr) : 
    mstr.lower()
    count = 0
    lstr = []
    for i in mstr :
        lstr.append(i)

    for j in range(len(lstr)) :
        if j+4 < len(lstr) :

            if lstr[j] == 'a' and lstr[j+4] == 'b' :
                count += 1
            elif lstr[j] == 'b' and lstr[j+4] == 'a' :
                count += 1
            else :
                count += 0
        else :
            count += 0

    if count > 0 :
        return "True"
    else :
        return "False"


mstr = input("Masukan Kalimat : ")

outp = checkAB(mstr)
print("Output : %s" % (outp))
