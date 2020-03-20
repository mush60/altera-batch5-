angka = input("Masukan Kumpulan angka : ")

def count_angka(angka) :
  lis = [int(x) for x in str(angka)]
  result = []
  dic = {}

  for i in range(10) :
    dic[i] = lis.count(i)

  for j in range(10) :
    if(dic[j] == 1) :
      result.append(j)
    
  return result



print(count_angka(angka))