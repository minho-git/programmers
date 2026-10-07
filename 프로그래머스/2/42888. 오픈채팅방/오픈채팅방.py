def solution(record):
    answer = []
    
    _dict = {}
    method = []
    id_list = []
    for r in record:
        if r[0] == "E":
            action, _id, name = r.split(" ")
            _dict[_id] = name
            id_list.append(_id)
            method.append(action)
            
        elif r[0] == "L":
            action, _id = r.split(" ")
            id_list.append(_id)
            method.append(action)
            
        else:
            action, _id, name = r.split(" ")
            _dict[_id] = name
        
    
    for i in range(len(method)):
        answer.append(_dict[id_list[i]] + "님이 들어왔습니다." if method[i][0] == "E" else _dict[id_list[i]] + "님이 나갔습니다.")
    
    return answer