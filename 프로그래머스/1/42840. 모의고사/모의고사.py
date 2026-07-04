def solution(answers):
    
    pattern = [
        [1, 2, 3, 4, 5], # 5
        [2, 1, 2, 3, 2, 4, 2, 5], # 8
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    ]
    
    result = []
    grades = [0, 0, 0]
    
    for index, value in enumerate(answers):
        for i in range(3):
            if value == pattern[i][index % len(pattern[i])]:
                grades[i] += 1
    
    max_grade = max(grades)
    for index, value in enumerate(grades):
        if value == max_grade:
            result.append(index+1)
    
    result.sort()
    return result