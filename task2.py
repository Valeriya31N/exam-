def palindrome(string: str) -> bool:
    return string == string[::-1]


text = input("Введите строку ")
print(palindrome(text))