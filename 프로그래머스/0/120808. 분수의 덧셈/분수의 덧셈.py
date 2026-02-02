import math

def solution(numer1, denom1, numer2, denom2):
    first = numer1 * denom2 + numer2 * denom1
    second = denom1 * denom2
    
    gcd = math.gcd(first, second)
    

    answer = [first//gcd, second//gcd]
    return answer