max = 0
maxNum = 0
for startNum in range(1, 1000000):
    n = startNum
    numTerms = 1
    while(n != 1):
        if(n%2 == 0):
            n /= 2
        else:
            n = 3*n+1
        numTerms += 1
    if(numTerms > max):
        max = numTerms
        maxNum = startNum

print(maxNum)
