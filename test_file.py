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


def defined(func, my_func, first=1000, second=1):
    # print("Try to call object from func variable:", func)
    return func(first, second) - my_func(first, second)

def multiplier(a, b):
    return a * b


def summarizer(power, a, *args, **kwargs):
    sum_num = 0
    for i_elem in args:
        sum_num += i_elem ** power
    return sum_num


print(summarizer(1,1, 2, 3, c=1, b=2))


# print(defined(multiplier,summarizer,10))
# print(defined(print, 10, 10))
# print(defined(summarizer, 10, 10))
# res = defined()
# print(res)


# print(defined)
# f = defined
# b = defined
# print(b, f)
# print(b(first=100), f(first=200))


def print_message():
    # print('Привет, мир.')
    def print_greeting():
        print('Привет, программист.')
    return str.split


# print(print_message())


# print(print, type(print))
# print(print_message)
# print(print_message())
# print(sum)
# print(print)
# print(divmod)
# print(type)
def deco(func):
    def wrapper(url):
        print("Покупайте наших котиков")
        return func(url)
    return wrapper

@deco
def make_request(url):
    print(f"Делаю запрос на {url}")
    return 123

# print(make_request(456))