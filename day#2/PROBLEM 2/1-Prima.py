#membuat fungsi yang parsing parameter dari inputan untuk di olah
def isPrime(n) :
    # membuat counter untuk menghitung apakah hasil n % i == 0
    count = 0
    if n < 1 :
        count += 1
    else :
        if n == 2 and n == 3 :
            count += 0
        else :
            for i in range(3, n) :
                if n % i == 0 :
                    # jika n % i == 0 true maka nilai count akan otomatis bertambah 1
                    count += 1
                else :
                    count += 0
    # membuat kondisi untuk mengetahui apakah count > 0, jika count > 0 maka not prime
    if count > 0 :
        return "Bukan Prime"
    else :
        return "Prime"




number = int(input("Masukan angka : "))

result = isPrime(number)

print("Bilangan %d adalah %s" % (number, result))