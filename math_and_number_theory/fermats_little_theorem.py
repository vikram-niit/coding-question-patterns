# fermat_little_theorem.py
# Checks Fermat's Little Theorem for given a and prime p

def is_prime(n):
    """Check if n is a prime number"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fermat_little_theorem(a, p):
    """Returns True if a^(p-1) ≡ 1 (mod p)"""
    if not is_prime(p):
        raise ValueError("p must be prime")
    if a % p == 0:
        raise ValueError("a must not be divisible by p")
    return pow(a, p-1, p) == 1

if __name__ == "__main__":
    a = int(input("Enter a (integer not divisible by p): "))
    p = int(input("Enter p (prime number): "))
    
    try:
        if fermat_little_theorem(a, p):
            print(f"{a}^{p-1} ≡ 1 (mod {p}) ✅ Fermat's Little Theorem holds")
        else:
            print(f"{a}^{p-1} ≢ 1 (mod {p}) ❌ Fermat's Little Theorem fails")
    except ValueError as e:
        print("Error:", e)
