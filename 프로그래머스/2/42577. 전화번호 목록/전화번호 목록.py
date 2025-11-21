def solution(phone_book):
    answer = True
    
    n = len(phone_book)
    phone_book.sort()
    # print(phone_book)
    
    cur = phone_book[0]
    for i in range(1, n):
        endIdx = len(cur)
        
        if cur ==  phone_book[i][0:endIdx]:
            return False
        else:
            cur = phone_book[i]

    return answer