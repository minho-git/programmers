def solution(s):
    s = s[1:-1]
    s = s.split("},{")
    s[0] = s[0].lstrip("{")
    s[-1] = s[-1].rstrip("}")
    
    s.sort(key = lambda x : len(x))
    
    for i in range(len(s)):
        s[i] = list(map(int, s[i].split(",")))
    
    check = {}
    answer = []
    for i in range(len(s)):
        for j in range(len(s[i])):
            if check.get(s[i][j], 0) == 0:
                answer.append(s[i][j])
                check[s[i][j]] = 1
    
    return answer