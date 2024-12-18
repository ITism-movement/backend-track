# # Декоратор 1 Оповещение о новом заказе с использованием аргументов функции
# def tg_message(func):
#     def wrapper(user,order_number,price,*args,**kwargs):
#         discounted_price = price*0.7
#         print(f"Добрый день, {user}! Спасибо за заказ в Ешки Матрешки. Номер вашего заказа {order_number}. "
#               f"Цена со скидкой 30% - {discounted_price} рублей.")
#         return func(user,order_number,price,*args, **kwargs)
#     return wrapper
#
# @tg_message
# def new_order(user,order_number,price):
#     return f"Заказ от пользователя {user} под номером {order_number} принят."
#
# # send_message = tg_message(new_order)
# # print(send_message("Антон М.", 1083, 1000))
#
# print(new_order("Антон М.", 1083, 1000))
# print(new_order)

# Декоратор 2
# Случай, когда необходимо использовать декоратор без "сахара"
# def discount(func):
#     def wrapper(*args, **kwargs):
#         discounted_price = func(*args, **kwargs)*0.7
#         return discounted_price
#     return wrapper
#
# @discount
# def new_order(cost, markup):
#     return cost + markup
#
# print(f"Цена без скидки {new_order(50,50)}. Цена со скидкой {discount(new_order)(50,50)}.")
# print(new_order)

# Декоратор 3 Рамка вокруг приветствия
# def frame(func):
#     def wrapper(*args):
#         name = f"*{func(*args)}*"
#         message_length = len(name)
#         star_line = "*"*message_length
#         return "\n".join([star_line,name,star_line])
#     return wrapper
#
# @frame
# def new_user(name):
#     return f"Hi {name}!"
# print(new_user("ITism"))

def decorator(func):
    def wrapper(*args,**kwargs):
        print("До")
        result = func(*args,**kwargs)
        print("После")
        return result
    return wrapper