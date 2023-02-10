def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def sum_of_gcd(N):
    sum = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            sum += gcd(i, j)
    return sum

N = 12
print("Sum of all GCDs : ", sum_of_gcd(N))



