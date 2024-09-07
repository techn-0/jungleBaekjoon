def solution(priorities, location):
    answer = 0
    
    while priorities:
        head = priorities.pop(0)
        if any(head < p for p in priorities):
            priorities.append(head)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else:
            answer += 1
            if location == 0:
                return answer
            location -= 1
