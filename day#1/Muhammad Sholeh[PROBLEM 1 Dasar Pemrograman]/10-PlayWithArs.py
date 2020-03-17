def generateSqr(num) :
    if num % 2 == 1 :
        stpl = int(num/2) #membuat batas atas kiri
        stpr = int(num/2)+1 #membuat batas atas kanan
        for i in range(num) :
            for j in range(num) :
                if(j not in range(stpl, stpr)) :
                    print(" ", end = " ")
                else :
                    print("*", end = " ")
            if(i < int(num/2)) :
                stpl -= 1
                stpr += 1
            else :
                stpl += 1
                stpr -= 1
            print("\t")
    else :
        print("=========== odd only ===========")
num = int(input("Masukan Bilangan : "))
generateSqr(num)