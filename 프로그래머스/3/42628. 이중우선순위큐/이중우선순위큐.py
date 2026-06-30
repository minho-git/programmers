import heapq

def solution(operations):
    
    idx = 0
    max_heap = []
    min_heap = []
    deleted_idx_set = set()
    
    for operation in operations:

        if operation[0] == "I":
            num = int(operation[2:])
            heapq.heappush(max_heap, (-num, idx))
            heapq.heappush(min_heap, (num, idx))
            idx += 1

        else:
            if len(operation) == 4: # "D -1"
                while min_heap:
                    popped = heapq.heappop(min_heap)
                    popped_idx = popped[1]
                    if popped_idx in deleted_idx_set:
                        continue
                    else:
                        deleted_idx_set.add(popped_idx)
                        break
                    
            else: # "D 1"
                while max_heap:
                    popped = heapq.heappop(max_heap)
                    popped_idx = popped[1]
                    if popped_idx in deleted_idx_set:
                        continue
                    else:
                        deleted_idx_set.add(popped_idx)
                        break
            
    # heap이 비었는지 체크
    # 리스트를 순회하면서 지우면 요소들이 밀려서 문제가 생김.
    # 리스트 컴프리핸션을 써서 새로운 리스트 할당하기
    min_heap = [(val, idx) for val, idx in min_heap if idx not in deleted_idx_set]
    max_heap = [(val, idx) for val, idx in max_heap if idx not in deleted_idx_set]
    
    heapq.heapify(min_heap)
    heapq.heapify(max_heap) 

    
    
    if not min_heap and not max_heap:
        return [0, 0]
        
    else:
        _min = heapq.heappop(min_heap)[0]
        _max = -heapq.heappop(max_heap)[0]
        return [_max, _min]
                