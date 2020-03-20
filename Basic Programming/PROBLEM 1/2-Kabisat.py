def kabisat(year) :
    if year % 400 != 0 :
        if year % 100 != 0 :
            if year % 4 != 0 :
                return "Bukan Tahun Kabisat"
            else :
                return "Tahun Kabisat"
        else :
            if year % 4 != 0 :
                return "Bukan Tahun Kabisat"
            else :
                return "Tahun Kabisat"
    else :
        return "Tahun Kabisat"

thn = int(input("Masukan tahun : "))

kab = kabisat(thn)

print("Tahun %d = %s" % (thn,kab))

