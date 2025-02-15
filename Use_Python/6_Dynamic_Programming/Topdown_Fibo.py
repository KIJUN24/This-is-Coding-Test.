d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    # 이미 계산한 적 있는 문제라면 그대로 반환환
    if d[x] != 0:
        return d[x]
    
    # 아직 계산하지 않은 문제라면 점화식에 따라 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
