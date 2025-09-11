N = int(input())
cycle = 0
startNumber = N

while True:
    일의자리 = N % 10 
    십의자리 = (N // 10)  

    새로운십의자리 = 일의자리  
    새로운일의자리 = ((십의자리 + 일의자리) % 10) 

    새로운수 = (새로운십의자리 * 10) + 새로운일의자리 
    cycle += 1 

    if 새로운수 == startNumber: 
        break

    N = 새로운수 


print(cycle)