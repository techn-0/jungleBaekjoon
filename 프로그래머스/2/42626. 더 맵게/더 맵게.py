import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0 #몇번 섞었는지
    
    while scoville:
        if scoville[0] >= K:
            return cnt
        
        if len(scoville) < 2:
            return -1
         
        fst = heapq.heappop(scoville)
        sec =  heapq.heappop(scoville)
        mixFood = fst + sec*2
        
        heapq.heappush(scoville, mixFood)
        cnt +=1

    return cnt