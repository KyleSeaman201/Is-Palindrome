# Function takes a string as a parameter and returns True if the string is a palindrome, False otherwise
def isPalindrome(text):
    # Reversing text
    if type(text) is not str:
        return False

    else:
        alphabet= "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        new_string=[]
        for i in text:
            if i in alphabet:
                new_string.append(i.lower())
        "".join(new_string)
        rev = new_string[::-1]
 
    # Checking if both strings are equal or not
    if (new_string == rev):
        return True
    else:
        return False

#test case
'''
print(isPalindrome("alula"))
print(isPalindrome("love"))
print(isPalindrome("Madam"))
print(isPalindrome(12))
print(isPalindrome(11))
print(isPalindrome(12.5))
print(isPalindrome(12.21))
print(isPalindrome("Mr. Owl ate my metal worm"))
print(isPalindrome([12, 21]))
'''