sequence = [2, 3, -6, 1, 3, -1, 2, 4]

def solution(sequence):
    n = len(sequence)

    pulse1 = [sequence[i] * (1 if i % 2 == 0 else -1) for i in range(n)]
    pulse2 = [sequence[i] * (-1 if i % 2 == 0 else 1) for i in range(n)]

    def kadane(arr):
        max_sum = float('-inf')
        curr_sum = 0
        for num in arr:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum

    return max(kadane(pulse1), kadane(pulse2))

print(solution(sequence))