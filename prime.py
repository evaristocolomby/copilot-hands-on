def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return not any(n % p == 0 or n % (p + 2) == 0 for p in range(5, int(n**0.5) + 1, 6))