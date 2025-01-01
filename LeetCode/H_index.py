class Solution(object):
    def hIndex(self, citations):
        # 인용 횟수를 내림차순으로 정렬
        citations.sort(reverse=True)
        
        h = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break
        
        return h
