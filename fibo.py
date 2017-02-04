def fibo(x):
    if x == 1:
        return 2
    if x == 0:
        return 1
    return fibo(x-1)+fibo(x-2)

n = 0
sum = 0
while True:
    term = fibo(n)
    if term > 4000000:
        break
    if term % 2 == 0:
        sum += term
    n += 1

print sum
