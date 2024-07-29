import string

def isPalindrome(str):
  str = str.lower()
  if (str == str[::-1]):
    return True
  else:
    return False


# Solicitar que o usuário digite a sentença
def main():
  userInput = input("Enter a WORD to be tested as a palindrome:")

  if (isPalindrome(userInput)):
    print(userInput + " is a palindrome!")
  else:
    print(userInput + " is NOT a palindrome!")

if __name__ == "__main__":
    main()