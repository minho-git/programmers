from datetime import date

def solution(today, terms, privacies):
    answer = []
    _dict = {}
    result = []
    
    now_year, now_month, now_day = map(int, today.split("."))
    today_date = date(now_year, now_month, now_day)
    
    for term in terms:
        category, duration = term.split(" ")
        _dict[category] = duration
        
    for privacie in privacies:
        _date, category = privacie.split(" ")
        year, month, day = map(int, _date.split("."))
        
        after_month = month - 1 + int(_dict[category])
        
        year += after_month // 12
        after_month = after_month % 12 + 1
        
        result.append(date(year, after_month, day))
    
    for i in range(len(result)):
        if today_date >= result[i]:
            answer.append(i+1)
        
        
        
    return answer