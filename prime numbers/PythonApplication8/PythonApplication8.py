#to exw kanei na bgainei me pinaka.den katalabaina to paradeigma


prime_numbers = [2,3,5,7,11,13,17]
power =[]


def analyze_number(n):
    n = (int)(n)
    for prime in prime_numbers:
        times = 0
        while n%prime == 0:
            print(" %10d - %2d " % (n, prime))
            times+=1
            n = n / prime

            
        power.append(times)

        if n==1:
            break

    print('prime numbers sample:' , (prime_numbers))
    print(power)


arithmos=input('give a number to analyze:  ')
analyze_number(arithmos)
