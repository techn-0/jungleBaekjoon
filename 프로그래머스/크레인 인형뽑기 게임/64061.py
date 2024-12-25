def solution(board, moves):
    answer = 0

    basket = [] # 바구니

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] == 0:
                continue
            else:
                basket.append(board[j][i-1])
                board[j][i-1] = 0 #뽑았으니 0으로
                if len(basket) > 1:
                    if basket[-1] == basket[-2]: #맨위에 2개 비교
                        basket.pop() #두개 터지니까 두번
                        basket.pop() # 어 왜 두번 써지지 어 왜 두번 써지지
                        answer += 2
            break
    return answer