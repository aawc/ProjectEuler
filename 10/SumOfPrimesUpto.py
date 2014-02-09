#!/usr/bin/python

import math

def IsPrime(n, primes_so_far):
  sqrt_n = int(math.sqrt(n))
  is_prime = True
  for _, prime in enumerate(primes_so_far):
    if prime > sqrt_n:
      break
    if not n % prime:
      is_prime = False
  #print n, is_prime
  return is_prime

def SumOfPrimesUpto(n):
  primes_so_far = []
  sum = 0
  for i in range(2, n):
    if IsPrime(i, primes_so_far):
      primes_so_far.append(i)
      sum += i
      print i, sum
  return sum

def main():
  N = 2000000
  print SumOfPrimesUpto(N)

if __name__ == '__main__':
  main()
