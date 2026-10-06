def solution(id_list, report, k):
    answer = []
    report_list = {}
    count_list = {}
    over_count_set = set()
    
    # 두 개의 자료구조가 필요하다.
    # {사람 : [신고한 사람들]}
    # {사람 : 신고당한 횟수}
    
    for id in id_list:
        report_list[id] = []
        count_list[id] = 0
        
    for tmp in report:
        _from, to = tuple(tmp.split(" "))
        
        if not to in report_list[_from]:
            report_list[_from].append(to)
            count_list[to] += 1
    
    
    for name, count in count_list.items():
        if count >= k:
            over_count_set.add(name)
    
    for key in report_list:
        tmp = 0
        for name in report_list[key]:
            if name in over_count_set:
                tmp += 1
        
        answer.append(tmp)
        
    return answer