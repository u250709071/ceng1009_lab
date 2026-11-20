# mylist = [[76, 92], "hello",True, 472,76]
# mylist.append(76)
# mylist.insert(3, "cat")
# mylist.insert(0, 99)
# print(mylist.index("hello"))
# print(mylist.count(76))
# print(mylist)
# mylist.remove(76)
# print(mylist)
# mylist.pop(mylist.index(True))
# print(mylist)



# def sum_of_squares(xs):
#     sum = 0
#     for l in xs:
#         sum += l**2
#     return sum
# print(sum_of_squares([1,2,3,4,5]))



# def sum_of_squares(xs):
#     sum = 0
#     for l in xs:
#         if l % 2 == 0:
#             sum += l ** 2
#     return sum
# print(sum_of_squares([1,2,3,4,5]))



# def length_word(xs):
#     counter = 0
#     for word in xs:
#         if len(word) == 5:
#             counter += 1
#     return counter
# print(length_word(["hello", "world", "GTA 6", "WAS", "RELEASED"]))



# def sum_of_numbers(xs):
#     sum = 0
#     for l in xs:
#         if l % 2 == 0:
#             break
#         else:
#             sum += l
#
#     return sum
# print(sum_of_numbers([7,9,5,4,11]))



# def length_word(xs):
#     counter = 0
#     for word in xs:
#         counter += 1
#         if word == "sam":
#             break
#     return counter
# print(length_word(["hello", "world", "GTA 6","sam", "WAS", "RELEASED"]))



# def replace(s, old, new):
#     pieces = s.split(old)
#     print(new.join(pieces))
#     return new.join(pieces)
# def test(actual, expected=None):
#     if expected is None:
#         print("NOT DEFINED")
#     elif actual == expected:
#         print("PASSED")
#     else:
#         print("FAILED")
#
# text = ("Hello Folks, Today we are gonna learn python modules in a hard way.First of all folks, "
#         "What are the types of data? You can say anyhing about it.But it's only some few data types in our world.")
# test(replace("Filks", "i", "I"), "FIlks")
# test(replace(text, "o", "Ü"))



# num_list = [1,16,31,43,24]
# def max(list):
#     highest = 0
#     for num in list:
#         if num > highest:
#             highest = num
#     return highest
# print(max(num_list))