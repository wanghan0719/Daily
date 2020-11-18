"""
    闭包的应用:
        逻辑连续
"""


# def give_gife_money(money):
#     def child_buy(target, price):
#         nonlocal money
#         if money >= price:
#             print("孩子购买", target, "花了", price, "钱")
#             money -= price
#             print('还剩%.1f'% money)
#         else:
#             print("钱不够，呜呜呜呜～")
#     return child_buy
#
#
# action = give_gife_money(10000)
# action("呲水枪", 100)
# action("飞机", 500)
# action("手机", 8848)
# action("火车", 500)
# action("老婆饼", 1500)


def print_func_name(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)

    return wrapper

# 需求：不改变原函数调用以及定义的情况下，增加新功能(打印函数名称)
@print_func_name
def say_hello():
    print("hello")
    # print(say_hello.__name__)

@print_func_name
def say_goodbye():
    print("goodbye")
    # print(say_goodbye.__name__)


say_hello()
say_goodbye()
