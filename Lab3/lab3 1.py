
s = input("Enter your string: ")

# Count the occurrences of each vowel (both lowercase and uppercase)
a = s.count('a')
b = s.count('e')  # Fixed variable name from 'bag.count' to 'b'
c = s.count('i')
d = s.count('o')
e = s.count('u')
f = s.count('A')
g = s.count('E')
h = s.count('I')
i = s.count('O')  # Fixed typo: '0' (zero) should be 'O' (uppercase o)
j = s.count('U')


P = a + b + c + d + e + f + g + h + i + j


print("The number of vowels in the string is", P)
