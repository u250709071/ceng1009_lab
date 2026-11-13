# def is_odd(n):
#     if n % 2 == 0:
#         return False
#     else :
#         return True
# output = is_odd(5)
# print(output)
import string
from cgitb import reset


# def is_leapyear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
# print(is_leapyear(2100))



# def print_triangular_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total = total + i
#         print(i, total)
#
# print(print_triangular_numbers(5))



# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# print(is_prime(51))



# def reverse1 (s):
#     result = ""
#     for ch in s:
#         result = ch + result
#     return result
# print(reverse1("hello world"))
#
# def reverse2 (s):
#     return s[::-1]
# print(reverse2("hello world"))



# def remove_all_occurences(sub, s):
#     return s.replace(sub, "")
# print(remove_all_occurences("ll", "hello world"))



# def substitute(message, key):
#     alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "qwertyuıopğüasdfghjklşizxcvbn"
# print(substitute("Hello World!", key))



def remove_dups(s):
    result = ""
    for ch in s:
        if ch.lower() not in result.lower():
            result = result + ch
    return result
print(remove_dups("Hello World"))


























