def solution(phone_book):
    phone_book.sort(key = lambda x:len(x))
    phone_book.reverse()
    
    _set = set()
    
    for phone_num in phone_book:
        if phone_num in _set:
            return False
        
        for i in range(1, len(phone_num)):
            _set.add(phone_num[:i])
        
    
    return True
        
        
#     while phone_book:
#         popped = phone_book.pop(0)

#         for phone in phone_book:

#             _length = len(popped)
#             if _length > len(phone):
#                 continue

#             if popped == phone[0:_length]:
#                 return False
        
#     return True