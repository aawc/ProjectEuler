#!/usr/bin/python

import math

def PrimeFactorsOf(n, factors_so_far):
  if n <= 1:
    factors_so_far[n] = {1}

  if (n not in factors_so_far):
    factors = {1, n}
    sqrt_n = int(math.sqrt(n))
    if n == sqrt_n * sqrt_n:
      factors.union(PrimeFactorsOf(sqrt_n, factors_so_far))

    for i in range(2, sqrt_n+1):
      if not n % i:
        factors_i = PrimeFactorsOf(i, factors_so_far)
        factors_ni = PrimeFactorsOf(n/i, factors_so_far)
        factors = factors.union(factors_i)
        factors = factors.union(factors_ni)

    factors_so_far[n] = factors

  #print n, factors_so_far[n]
  return factors_so_far[n]

def HighlyDivisibleTriangularNumber(number_of_divisors):
  next_add = 1
  current_base = 0
  factors_so_far = dict()
  while True:
    current_base += next_add
    next_add += 1
    factors = PrimeFactorsOf(current_base, factors_so_far)
    if (len(factors) > number_of_divisors):
      print current_base, number_of_divisors, factors
      return current_base

def main():
  NUMBER_OF_DIVISORS = 500
  print HighlyDivisibleTriangularNumber(NUMBER_OF_DIVISORS)

if __name__ == '__main__':
  main()
