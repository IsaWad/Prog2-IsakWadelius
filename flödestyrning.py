# 1. Gör ett program som skriver ut alla tal under 1000 som är jämnt delbara med 7.
def upg_ett():
    tal = []
    for i in range(1000):
        if i % 7 == 0:
            tal.append(i)
    print(tal)

# 2. Gör ett program som räknar antalet siffror i en godtycklig inmatad textsträng.
def upg_två():
    siffror = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    siffrorITal = []
    str = "Hej76k"
    for i in range(len(str)):
        if str[i] in siffror:
            siffrorITal.append(str[i])
    print(len(siffrorITal))

# 3. Gör ett program som hittar det 1000e primtalet. Använd modulooperatorn (%) för att undersöka delbarhet.

def upg_tre():
    prime = [1]
    #used = [1]
    num = 0
    while True:
        print(num)
        #print(used)
        #print(range(num))
        num += 1
        if len(prime) == 1000:
            break
        a = 2
        for a in range(num):
            if num % a == 0:
                continue
            else:
                prime.append(num)
            a +=1
#upg_tre()

def generate_primes():
    """
    Generate the first 'n' prime numbers.
    
    :param n: The number of prime numbers to generate.
    :return: A list of the first 'n' prime numbers.
    """
    primes = []
    num = 2  # Start with the first prime number, 2.
    n = 100
    while len(primes) < n:
        is_prime = True
        
        # Check if 'num' is divisible by any of the previously found primes.
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

        # Move on to the next number.
        num += 1
    return primes

# Example usage:
num_primes_to_generate = 1000  # Change this to generate a different number of primes.
prime_list = generate_primes(num_primes_to_generate)
print(prime_list)

