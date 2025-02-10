result = 0
n, k = map(int, input().split())
target = (n // k) * k
result += n - target

result += 1
n //= k

result += (n-1)

print(result)