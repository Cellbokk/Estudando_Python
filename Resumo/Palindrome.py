import string

def isPalindrome(str):
    exclude = set(string.punctuation)
    str = ''.join(ch for ch in str if ch not in exclude)
    str = str.replace(" ", "").lower()

    if str == str[::-1]:
        return True
    else:
        return False

def main():
    userSentence = input("Enter a sentence to be tested as a palindrome:")

    if isPalindrome(userSentence):
        print(userSentence + " is a palindrome!")
    else:
        print(userSentence + " is NOT a palindrome!")

if __name__ == "__main__":
    main()
