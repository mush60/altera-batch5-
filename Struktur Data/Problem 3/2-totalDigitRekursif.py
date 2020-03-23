def totalDigitRekursif(num, jum = 0) :
    if num > 9 :
        str_num = str(num)
        jum += int(str_num[0:1])
        str_num = str_num[1::]
        num = int(str_num)
        return totalDigitRekursif(num, jum)
    else :
        if jum != 0 :
            return num + jum
        else :
            return num


print(totalDigitRekursif(512))
print(totalDigitRekursif(1524))
print(totalDigitRekursif(5))
print(totalDigitRekursif(21))
print(totalDigitRekursif(11111))
    