def solution(brown, yellow):
    
    total = brown + yellow
    answer = 0
    
    # (w-2) * (h-2) = yellow 라는 공식으로 부터 시작해서
    # h를 3부터 시작해서 int(total ** 0.5) + 1까지 돌면서
    # w를 찾아서, 위 공식이 성립하는지 보고 성립하면 정답
    
    for h in range(3, int(total ** 0.5) + 1):
        if total % h == 0:
            w = total // h
            if (w-2) * (h-2) == yellow:
                answer = [w, h]
            
    return answer