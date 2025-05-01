def count_alphabets_digits(s):
    count = sum(1 for char in s if char.isalpha())  
    digit_count = sum(1 for char in s if char.isdigit())
    return count, digit_count


s = input("Enter a string: ")


count, digit_count = count_alphabets_digits(s)


print(f"Number of alphabets: {count}")
print(f"Number of digits: {digit_count}")
