def solution(players, callings):
    answer = []
    
    ranks = {}
    reverse_ranks = {}
    
    for i in range(len(players)):
        ranks[i] = players[i]
        reverse_ranks[players[i]] = i
        
    
    for name in callings:
        rank = reverse_ranks[name]
        tmp = ranks[rank-1]
        
        ranks[rank-1] = name
        reverse_ranks[name] = rank-1
        
        ranks[rank] = tmp
        reverse_ranks[tmp] = rank
        
        
    
    return list(ranks.values())
    