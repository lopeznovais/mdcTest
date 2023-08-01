def is_palindrome(word):
    word = word.lower()
    return "Is palindrome" if word == word[::-1] else "Is not palindrome"

word = input("Enter a word ")
print(is_palindrome(word))