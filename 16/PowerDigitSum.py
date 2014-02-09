#!/usr/bin/python

def PowerDigitSum(n):
  sum = 0
  for n in str(2 ** n):
    sum += int(n)
  return sum

def main():
  N = 1000
  print PowerDigitSum(N)

if __name__ == '__main__':
  main()
