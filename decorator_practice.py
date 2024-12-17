# Декоратор 1 Оповещение о новом заказе с использованием аргументов функции
def tg_message(func):
    def wrapper(*args, **kwargs):
        discounted_price = args[2]*0.7
        print(f"Добрый день, {args[0]}! Спасибо за заказ в Ешки Матрешки. Номер вашего заказа {args[1]}. "
              f"Цена со скидкой 30% - {discounted_price} рублей.")
        return func(*args, **kwargs)
    return wrapper

def new_order(user,order_number,price):
    return f"Заказ от пользователя {user} под номером {order_number} принят."

send_message = tg_message(new_order)
print(send_message("Антон М.", 1083, 1500))


# Декоратор 2
# Случай, когда необходимо использовать декоратор без "сахара"
def discount(func):
    def wrapper(*args, **kwargs):
        discounted_price = func(*args, **kwargs)*0.7
        return discounted_price
    return wrapper

def new_order(cost, markup):
    return cost + markup

print(f"Цена без скидки {new_order(50,50)}. Цена со скидкой {discount(new_order)(50,50)}.")


# Декоратор 3 Рамка вокруг приветствия
def frame(func):
    def wrapper(*args):
        name = f"*{func(*args)}*"
        message_length = len(name)
        star_line = "*"*message_length
        return "\n".join([star_line,name,star_line])
    return wrapper

@frame
def new_user(name):
    return f"Hi {name}!"

print(new_user("Zarina"))