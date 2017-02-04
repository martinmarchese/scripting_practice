def isPrime(x):
    i = 2
    while True:
        if x % i == 0 or i == x:
            break
        i += 1
    if i == x:
        return True
    return False

j = 0
for i in range(2,101):
    if(isPrime(i)):
        print str(i)
        j += 1
print j
