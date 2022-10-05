def primes(number_of_primes):
  def is_prime(n):
    for i in range(2,n):
      if (n%i) == 0:
        return False
    return True
  list = []
  if (number_of_primes > 0):
    n=2  
    while len(list) < number_of_primes:
      if (is_prime(n)):
        list.append(n)
      n+=1
    return list
  else:
    raise ValueError