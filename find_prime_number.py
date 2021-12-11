def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return "is not prime"

    return 'is prime'
    
print(prime_number(3))