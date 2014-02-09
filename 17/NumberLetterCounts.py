#!/usr/bin/python

# The count for the first hundred numbers repeats 10 times, once for each
# century, so let's count that first:
# one appears in all 10x+1 cases, except eleven, so: nine times
# same for two, three, four, five, six, seven, eight, nine
# that is:
length_of_one_to_nine = (3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4)
length_of_one_to_nine_in_first_hundred = length_of_one_to_nine * 9

# Each series of ten has the same prefix, for instance twenty, thirty, etc.
# So:
tens_prefixes = (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) * 10

# Now for 10 - 19:
# So:
ten_to_nineteen = (3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8)

# Total for the first hundred numbers:
first_hundred = (
    length_of_one_to_nine_in_first_hundred + tens_prefixes + ten_to_nineteen)

# Calculating the hundred prefix:
hundredand_prefix_length = len('hundredand') * 99
hundred_prefix_length = len('hundred')
digit_prefix_length = 100 * length_of_one_to_nine
total_hundred_prefixes = (
    9 * (hundredand_prefix_length + hundred_prefix_length) +
    digit_prefix_length)

length_of_one_thousand = 3 + 8

# The first_hundred repeats 10 times, out of which 9 times have the additional
# hundred prefix.
total = first_hundred * 10 + total_hundred_prefixes + length_of_one_thousand

print total
