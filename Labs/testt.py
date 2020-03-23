def reverse(kata):
    return kata[::-1]

def lowerUpper(kata):
    new_kata = ''
    for c in kata:
        ord_c = ord(c)
        if ord_c in range(65, 91):
            c = c.lower()
        elif ord_c in range(97, 123):
            c = c.upper()
        new_kata += c
    return new_kata

def removeSpace(kata):
    new_kata = ''
    for i in kata :
        if ord(i) != 32 :
            new_kata += i
    return new_kata


print(removeSpace('tE sT'))