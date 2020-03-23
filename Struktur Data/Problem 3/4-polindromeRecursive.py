def polindromeRecursive(sentenc) :
    if len(sentenc) < 2 :
        return True
    else :
        if sentenc[0] == sentenc[-1] :
            return polindromeRecursive(sentenc[1:len(sentenc)-1])
        else :
            return False

print(polindromeRecursive('katak'))
print(polindromeRecursive('blanket'))
print(polindromeRecursive('civic'))
print(polindromeRecursive('kasur rusak'))
print(polindromeRecursive('mister'))