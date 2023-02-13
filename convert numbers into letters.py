"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"

Example 4:
Input: 52
Output: "AZ"



def convertToTitle(n):
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    while n > 0:
        remainder = n % len(alphabet)
        if remainder == 0:
            result = alphabet[len(alphabet) - 1] + result
            n = n // len(alphabet) - 1
            
        else: #n % len(alphabet) != 0
            result = alphabet[remainder - 1] + result
            n = n // len(alphabet)

    return result
            
        
print(convertToTitle(1))            
print(convertToTitle(28))
print(convertToTitle(701))
print(convertToTitle(52))
print(convertToTitle(27))        
            
""" 

digits = "012345679"
base = len(digits)


def base26excel(n):
    result = ""

    while n:
        n -= 1
        result = digits[n % base] + result
        n //= base

    return result

  
print(" ")
print(convertToTitle(1))            
print(convertToTitle(28))
print(convertToTitle(701))
print(convertToTitle(52))
print(convertToTitle(27))

"""
for i in range(1, 20 + 1):
    print(base26excel(i))

""" 
