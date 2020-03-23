def fabonaciRecursif(num, fbn = []) :
    if num <= 1 :
        return num
    else :
        if len(fbn) == num+1 :
            return fbn[len(fbn)-1]
        elif len(fbn) == 0 :
            fbn.extend([0, 1, 1])
            return fabonaciRecursif(num, fbn)
        else :
            fbn.append(fbn[len(fbn)-2] + fbn[len(fbn)-1])
            return fabonaciRecursif(num, fbn)

print(fabonaciRecursif(0))
print(fabonaciRecursif(1))
print(fabonaciRecursif(2))
print(fabonaciRecursif(9))
print(fabonaciRecursif(10))
print(fabonaciRecursif(12))
# print(fabonaciRecursif(90))
# print(fabonaciRecursif(100))

