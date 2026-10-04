def solution(name, yearning, photo):
    answer = []
    
    점수판 = {}
    for i in range(len(name)):
        점수판[name[i]] = yearning[i]
        
    for 사진 in photo:
        total = 0
        for 사람 in 사진:
            total += 점수판.get(사람, 0)
    
        answer.append(total)
        
    return answer