def convertMnt(mnt) :
    jam = 0
    if mnt % 60 == 0 :
        jam = int(mnt / 60)
        snmnt = '00'
        return str(jam)+':'+snmnt

    else :
        jam = int(mnt/60)
        if mnt % 60 > 9 :
            snmnt = str(mnt%60)
        else :
            snmnt = '0'+str(mnt%60)
        return str(jam)+':'+snmnt

mnt = int(input("Masukan Jumlah Menit : "))

waktu = convertMnt(mnt)

print("Hasil Konversi yaitu = %s " % (waktu))