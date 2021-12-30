def isMultThreeOrFive(n):
    if(n % 3 == 0 or n % 5 == 0):
        return True
    else:
        return False


sum = 0
for x in range(1000):
    if(isMultThreeOrFive(x)):
        sum+=x


print(sum)
