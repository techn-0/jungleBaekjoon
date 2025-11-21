def solution(genres, plays):
    answer = []
    n = len(genres)
    
    dicGenres = {}
    for i in genres:
        if i in dicGenres:
            dicGenres[i] += 1
        else:
            dicGenres[i] = 1
    # print(dicGenres)
    
    cntPlay = {}
    for i in dicGenres.keys():
        cntPlay[i] = 0

    for i in range(n):
        # print(plays[i])
        cntPlay[genres[i]] += plays[i]
    
    cntPlay = dict(sorted(cntPlay.items(), key=lambda item: item[1], reverse = True))
    
    
    songs = []
    for g, _ in cntPlay.items():
        songs = []
        for i in range(n):
            curr = 0
            if genres[i] == g:
                songs.append((i, plays[i]))
        songs.sort(key = lambda x : (-x[1], x[0]))
        
        for i, p in songs[:2]:
            answer.append(i)
            
            

    return answer