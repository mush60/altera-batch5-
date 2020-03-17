def generateAngka(num) :
    new_num = num
    temp = 0
    while new_num > 0 :
        stn = new_num % 10
        temp = temp * 10 + stn
        new_num = int(new_num/10)

    print(temp)

n = int(input("Masukan angka : "))
generateAngka(n)