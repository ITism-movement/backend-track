# itism = ['I', 't', 'i', 's', 'm']
# for i in range(4):
#     print(''.join(itism))
# print('The end.')
# a = int(input("Please enter first number: "))
# b = int(input("Please enter second number: "))
# sum_ab = a + b
# #commented by Ilia
# #321 comment by Lera
# # This is Zarina's comment
# # 123 commented by Ivan
# print("The sum of the numbers is", sum_ab)


a = 1
# print(type(a))


def defined(func, first=1000, second=1):
    return func(first, second)

def multiplier(a, b):
    return a * b

# print(defined(multiplier(10,10),10,10))
# res = defined()
# print(res)


# print(defined)
# f = defined
# b = defined
# print(b, f)
# print(b(first=100), f(first=200))

def print_message():
    print('Привет, мир.')
    def print_greeting():
        print('Привет, программист.')
    return print_greeting

print(print_message())

