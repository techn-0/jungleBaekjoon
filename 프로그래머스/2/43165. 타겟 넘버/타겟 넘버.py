def solution(numbers, target):
    def dfs(idx, curr):
        if idx >= len(numbers):
            if curr == target:
                return 1
            else:
                return 0
        return dfs(idx + 1, curr + numbers[idx]) +dfs(idx + 1, curr - numbers[idx])
    answer = dfs(0, 0)
    return answer