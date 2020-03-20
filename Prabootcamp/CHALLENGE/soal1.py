
user_in = input("Masukan Nilai : ")

n = int(user_in)

if n > 100 and n < 1 :
  print("Nilai di luar range 1-100")
else :
  if n > 79 :
    print("A")
  elif n > 64 :
    print("B")
  elif n > 49 :
    print("C")
  elif n > 34 :
    print("D")
  else :
    print("E")
  