def BigPartner(num) :
    snum = str(num)
    lres = []
    if len(snum) % 2 == 0 :
        lnum = []
        for i in snum : 
            lnum.append(i)
        
        for j in range(0, len(lnum), 2) :
            lres.append(int(lnum[j]+""+lnum[j+1]))
        return str(max(lres))
    else :
        return "===== panjang inputan harus genap ====="


numIn = int(input("Masukan beberapa digit angka : "))

hasil = BigPartner(numIn)
print("Output : {0}".format(hasil))

