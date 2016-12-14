n = int(input())

for i in range(len(str(n))):
    m = (10 ** (i + 1))
    if n % m >= 5 * (10 ** i):
        n += m - n % m
print(n)
