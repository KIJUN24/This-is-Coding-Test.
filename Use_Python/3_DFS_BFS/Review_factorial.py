# 반복적으로 구현한 팩토리얼
def factorial_for(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱
    for i in range(1, n+1):
        result *= i
    return result



# 재귀적으로 구현한 팩토리얼
def factorial_recursive(n):
    # n이 1이하인 경우 1을 반환
    if n <= 1:
        return 1
    
    # n! = n * (n-1)! 을 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

print("반복적으로 구현 : ", factorial_for(5))
print("재귀적으로 구현 : ", factorial_recursive(5))