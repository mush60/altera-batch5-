def convertIntToList(n) :
    number = []
    current_number = n
    reversed_number = []
    while current_number > 0 :
        last_digit = current_number % 10
        reversed_number.append(last_digit)
        current_number = (current_number - last_digit) // 10
    for i in range(len(number)) :
        reversed_number[i] = number[len(number)-1 -i]
    return(reversed_number)
    
    
    
    

angka = int(input("Masukan integer : "))

print(convertIntToList(angka))
