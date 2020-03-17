strx = 'coba coba'
str2 = ''
l = len(strx)
# for i in range(len(strx)) :
#     str2 = str2 + strx[l-1]
#     l -= 1

while l > 0 :
    str2 = str2 + strx[l-1]
    l -= 1

print(str2)