# List Sample 1
#---------------------------------------------
# msg = 'hello world!'
# print(msg)
# list_msg = list()
# list_msg = list(msg)
# print(list_msg)
# tuple_msg = tuple()
# tuple_msg = tuple(msg)
# print(tuple_msg)
# x = list_msg
# print(x)
# let = 'a'
# for i in range(0,len(msg),3):
#  x[i] = let
# print(x)
# list_msg.reverse()
# print(list_msg)
# list_msg.sort()
# print(list_msg)
# a = list_msg.pop()
# print(a)
# a = 'x'
# list_msg.append(a)
# print(list_msg)
# a = 'm'
# list_msg.insert(9,a)
# print(list_msg)
# print(max(list_msg))
# print(min(list_msg))

# List Sample 2
#---------------------------------------------
# lst = []
#
# x = int(input("how many values to be inserted in the list: "))
#
# for i in range(1, x+1):
#     a = input("value: ")
#     lst.append(a)
#
# for i in range(len(lst)):
#     print(lst[i])
#
# print(lst)
# lst.sort()
# print(lst)

# List Sample 3
#---------------------------------------------
# st = "hello world"
# lst = list(st)
# print(lst)
# lst.insert(4, str(3))
# print(lst)
# lst.pop()
# lst.sort()
# print(lst)
# lst.remove('l')
# print(lst)
# lst.reverse()
# print(lst)

# Tuple Sample 1
#---------------------------------------------
# tpl = tuple()
# lst = []
# x = int(input("how many values to be inserted in the list: "))
# for i in range(i, x+1):
#     a = input("value: ")
#     lst.append(a)
# tpl = tuple(lst)
# for i in range(len(tpl)):
#     print(tpl[i])
# print(tpl)
# lst = list(tpl)
# tpl = tuple(lst)
# print(tpl)

# Dictionary Sample 1
#---------------------------------------------
Dictionary1 = {'A': 'Geeks', 'B': 'For'}
Dictionary2 = {'B': 'Geeks'}

#Dictionary before Update
print("Original Dictionary")
print(Dictionary1)

Dictionary1.update(Dictionary2)
print("Dictionary After Update")
print(Dictionary1)

Dictionary1.update(B = 'For', C = 'Geeks')
print("Dictionary After Update")
print(Dictionary1)

# Dictionary Sample 2
#---------------------------------------------
# dic1 = {}
# a = input('name: ')
# b = int(input('age: '))
# dic1.update({'Name1': a, 'Age1': b})
# dic1.update(dic1)
# # print(dic2)
# print()
# a = input('name: ')
# b = int(input('age: '))
# dic1.update({'Name2': a, 'Age2': b})
# dic1.update(dic1)
# # print(dic2)
# print()
# a = input('name: ')
# b = int(input('age: '))
# dic1.update({f'Name3': a, 'Age3': b})
# dic1.update(dic1)
# print()
# print(dic1)

# Dictionary Sample 3
#---------------------------------------------
# dic1 = {}
# for i in range(0,3):
#  a = input('name#' + str(i+1) + ': ')
#  b = int(input('age#' + str(i+1) + ': '))
#  dic1.update({'Name#'+ str(i+1): a, 'Age#' + str(i+1): b})
#  dic1.update(dic1)
#  print()
# print(dic1)