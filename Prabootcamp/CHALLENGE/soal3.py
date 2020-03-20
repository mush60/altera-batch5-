user_in = input("Masukan Nomor : ")

n = int(user_in)
a = 1
for x in range(n) :
  for y in range(n) :
    print((x+1)* (y+1), end = " ")
    a += 1
  print("")
