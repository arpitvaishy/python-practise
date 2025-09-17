def custom_sort(s):
    lowercase = []
    uppercase = []
    odd_digits = []
    even_digits = []

    for char in s:
        if char.islower():
            lowercase.append(char)
        elif char.isupper():
            uppercase.append(char)
        elif char.isdigit():
            if int(char) % 2 == 0:
                even_digits.append(char)
            else:
                odd_digits.append(char)

    lowercase.sort()
    uppercase.sort()
    odd_digits.sort()
    even_digits.sort()

    return ''.join(lowercase + uppercase + odd_digits + even_digits)

# Input from user
s = input()
print(custom_sort(s))
