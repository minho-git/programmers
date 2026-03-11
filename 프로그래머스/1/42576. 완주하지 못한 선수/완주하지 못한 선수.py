from collections import Counter

def solution(participant, completion):

    dif = Counter(participant) - Counter(completion)
    dif = list(dif.keys())[0]

    return dif