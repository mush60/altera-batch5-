def kaliTerusRecursif(num) :
    if num > 9 :
        new_num = num
        list_num = []
        while new_num > 0 :
            single_num = new_num % 10
            list_num.insert(0,single_num)
            new_num = new_num // 10
        hasil_kali = 1
        for i in list_num :
            hasil_kali = hasil_kali * i            
        return kaliTerusRecursif(hasil_kali)
    else :
        return num


print(kaliTerusRecursif(66))
print(kaliTerusRecursif(3))
print(kaliTerusRecursif(24))
print(kaliTerusRecursif(654))
print(kaliTerusRecursif(1231))
print(kaliTerusRecursif(0))
