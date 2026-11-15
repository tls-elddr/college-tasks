def primes(start: int, end: int) -> list[int] | None:
  def is_prime(num: int) -> bool:
    if num < 2:
      return False
    for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
        return False
    return True
​
  result = [n for n in range(max(2, start), end + 1) if is_prime(n)]
  return result if result else None
​
​