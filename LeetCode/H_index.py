class Solution(object):
    def hIndex(self, citations):
        # 인용 횟수를 내림차순으로 정렬
        citations.sort(reverse=True)
        
        h = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1: # i+1 ;  현재 확인한 논문 수
            # 현재까지 확인한 논문의 개수보다 인용 횟수가 크거나 같은가
                h = i + 1
            else:
                break
        
        return h
