numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for number in numbers:
    if number < 2:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

del not_primes[0]
print("Primes:", primes)
print("Not primes:", not_primes)
