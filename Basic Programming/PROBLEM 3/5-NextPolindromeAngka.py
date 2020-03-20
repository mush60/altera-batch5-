def nextPalindrome(n) :
    count = 0
    hasil = 0
    
    while count < 1 :
        n += 1
        new_angka = n
        temp = 0
        while new_angka > 0 :
            satuan = new_angka % 10
            temp = temp * 10 + satuan
            new_angka = int(new_angka/10)
        if n == temp :
            hasil = temp
            count += 1

    # print(hasil)
    return hasil
    



angka = int(input("Masukan integer : "))

res = nextPalindrome(angka)
print("Next Palindrome Angka : {0}".format(res))
