user_in = input("Masukan Nomor : ")

n = int(user_in)
a = 1
for x in range(n) :
  for y in range(n) :
    if(a % 3 == 0) :
      print("*", end = " ")
    elif(a % 2 == 0) :
      print("$", end = " ")
    else :
        print("@", end = " ")
    a += 1
  print("")
