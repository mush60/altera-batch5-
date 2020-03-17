def loopFor(tstr, jlop, bc) :
    print("This is for loop")
    for i in range(0+bc, jlop+bc, bc) :
        print("%d - %s" % (i, tstr))

def whileLoop(tstr, jlop, bc) :
    print("This is while loop")
    i = 0
    while i < jlop :
        print("%d - %s" % (i+2, tstr))
        i += bc

str1 = input("Masukan string 1 : ")
str2 = input("Masukan string 2 : ")
jlop = int(input("Masukan Jumlah Perulangan : "))
bc = int(input("Masukan Jump range (ex : 2) : "))

loopFor(str1, jlop, bc)
whileLoop(str2, jlop, bc)

