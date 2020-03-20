instr = input("Masukan String : ")
instr = instr.lower()

def rotate10(num) :
  if num in range(97, 113) :
    num += 10
    return num
  elif num in range (113, 123) :
    num = 96 + abs(112 - num)
    return num
  else :
    return num

res = ""

for i in instr :
  res += (str(""+chr(rotate10(ord(i)))))

print(res.upper())