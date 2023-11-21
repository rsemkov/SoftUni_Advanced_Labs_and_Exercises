def palindrome(word, idx):
    if word == word[-1::-1]:
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"


print(palindrome("peter", 0))
