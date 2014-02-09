#!/usr/bin/python

def GetCollatzSequenceFor(n, known_sequences):
  if n not in known_sequences:
    sequence = [n]
    if n > 1:
      next_n = 3*n+1 if n%2 else n/2
      sequence.extend(GetCollatzSequenceFor(next_n, known_sequences))
      #print n, next_n, sequence
    known_sequences[n] = sequence

  return known_sequences[n]

def LongestCollatzSequenceUnder(n):
  known_sequences = dict()
  longest_n = -1
  longest_len = 0
  for i in range(1, n):
    sequence = GetCollatzSequenceFor(i, known_sequences)
    if longest_len < len(sequence):
      longest_len = len(sequence)
      longest_n = i
      #print 'New: ', longest_len, longest_n, sequence
  return longest_n

def main():
  N = 1000000
  #N = 13
  print LongestCollatzSequenceUnder(N)

if __name__ == '__main__':
  main()
