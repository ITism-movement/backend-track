# itism = ['I', 't', 'i', 's', 'm']
# for i in range(4):
#     print(''.join(itism))
# print('The end.')
# a = input("Please enter first number: ")
# b = input("Please enter second number: ")
# sum_ab = a + b
# #commented by Ilia
# #321 comment by Lera
# # This is Zarina's comment
# # 123 commented by Ivan
# print("a and b is", sum_ab)


a = 1
# print(type(a))


def defined(first=1000, second=1):
    return first + second

# res = defined()
# print(res)


print(defined)
f = defined
b = defined
print(b, f)
print(b(first=100), f(first=200))
