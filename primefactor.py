def isPrime(x):
    i = 2
    while True:
        if x % i == 0 or i == x:
            break
        i += 1
    if i == x:
        return True
    return False

num = 600851475143
l = 600851475143
found = False

while True:
    print("Testing is Prime for: " + str(l) + "...")
    if isPrime(l) and num % l == 0:
        maxPrimeFactor = l
        found = True
        break
    l -= 1


print "FOUND!! Max Prime Factor is: " + str(maxPrimeFactor)
