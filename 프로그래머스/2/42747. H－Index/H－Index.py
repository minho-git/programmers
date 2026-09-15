def solution(citations):
    
# 제출 전 사고 질문
    # 오름차순 정렬 후 인덱스 i에서 인용 횟수가 citations[i] 이상인 논문은 적어도 몇 편인가요?

    # 처음으로 조건을 만족한 n - i가 최대 H인 이유를 설명하세요.
    
    # H는 반드시 배열 원소 중 하나여야 하나요? 반례로 답하세요.
    
    # 가능한 H를 모두 검사하는 풀이와 정렬 후 한 번 순회하는 풀이를 비교하세요.
    
    answer = 0
    n = len(citations)    
    citations.sort(reverse=True)
    _max = citations[0]
    
    for i in range(_max, -1, -1):
        count = 0
        for j in citations:
            if i <= j:
                count += 1
            else:
                break
        
        if count >= i:
            answer = i
            break
        
    return answer