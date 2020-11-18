"""
    装饰器推导过程
"""


# 缺点：多个函数，具有相同代码(验证权限)
# def enter_background():
#     print("验证权限")
#     print("进入后台喽")
# def delete_order():
#     print("验证权限")
#     print("删除订单")

# 缺点：需要调用验证权限方法，又有可能不调用。
# def verif_permissions():
#     print("验证权限")
#
# def enter_background():
#     verif_permissions()
#     print("进入后台喽")
#
# def delete_order():
#     verif_permissions()
#     print("删除订单")

# 缺点：在调用原有功能前，需要为原有功能重新赋值（拦截）
# def verif_permissions(func):
#     def wrapper():
#         print("验证权限")
#         func()
#     return wrapper
#
# def enter_background():
#     print("进入后台喽")
#
# def delete_order():
#     print("删除订单")
#
# #  内部函数 = 原有功能 + 验证权限
# enter_background = verif_permissions(enter_background)
# enter_background()
# #   内部函数 = 原有功能 + 验证权限
# delete_order = verif_permissions(delete_order)
# delete_order()

# def verif_permissions(func):
#     def wrapper():
#         print("验证权限")
#         func()
#     return wrapper
#
# #enter_background = verif_permissions(enter_background)
# @verif_permissions
# def enter_background():
#     print("进入后台喽")
#
# @verif_permissions
# def delete_order():
#     print("删除订单")
#
# enter_background()
#
# delete_order()

def verif_permissions(func):
    def wrapper(*args, **kwargs):  # (101,)  {}
        print("验证权限")
        re = func(*args, **kwargs)  # 调用原有函数
        return re  # 内部函数返回 原有函数结果

    return wrapper


# enter_background = verif_permissions(enter_background)
@verif_permissions
def enter_background():  # --> wrapper
    print("进入后台喽")
    return "ok"


@verif_permissions
def delete_order(oid):  # wrapper
    print("删除订单")


# re = enter_background()# wrapper
# print(re)

delete_order(101)
