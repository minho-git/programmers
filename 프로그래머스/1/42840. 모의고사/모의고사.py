def solution(answers):
    
    grade1 = 0
    grade2 = 0
    grade3 = 0

    for i in range(len(answers)):
        if i % 5 == 0:
            if answers[i] == 1:
                grade1 += 1
        elif i % 5 == 1:
            if answers[i] == 2:
                grade1 += 1
        elif i % 5 == 2:
            if answers[i] == 3:
                grade1 += 1
        elif i % 5 == 3:
            if answers[i] == 4:
                grade1 += 1
        elif i % 5 == 4:
            if answers[i] == 5:
                grade1 += 1
    
    for i in range(len(answers)):
        if i % 2 == 0:
            if answers[i] == 2:
                grade2 += 1
        elif i % 8 == 1:
            if answers[i] == 1:
                grade2 += 1
        elif i % 8 == 3:
            if answers[i] == 3:
                grade2 += 1
        elif i % 8 == 5:
            if answers[i] == 4:
                grade2 += 1
        elif i % 8 == 7:
            if answers[i] == 5:
                grade2 += 1            
    
    for i in range(len(answers)):
        v = i % 10
        if v in [0, 1]:
            if answers[i] == 3:
                grade3 += 1
        elif v in [2, 3]:
            if answers[i] == 1:
                grade3 += 1
        elif v in [4, 5]:
            if answers[i] == 2:
                grade3 += 1
        elif v in [6, 7]:
            if answers[i] == 4:
                grade3 += 1
        elif v in [8, 9]:
            if answers[i] == 5:
                grade3 += 1      
        
    answer = []
    
    grades = [grade1, grade2, grade3]
    max_value = max(grades)
    
    
    for i in range(len(grades)):
        if grades[i] == max_value:
            answer.append(i+1)
    answer.sort()
    return answer