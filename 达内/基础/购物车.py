class ShoppingModel:
    dict_commodity_info = {
        101: {"name": "屠龙刀", "price": 10000},
        102: {"name": "倚天剑", "price": 10000},
        103: {"name": "九阴白骨爪", "price": 8000},
        104: {"name": "九阳神功", "price": 9000},
        105: {"name": "降龙十八掌", "price": 8000},
        106: {"name": "乾坤大挪移", "price": 10000}
    }


class ShoppingView:
    def __init__(self):
        self.__controller = ShoppingController()

    def shopping(self):
        while True:
            self.__display_menu()
            self.__select_menu_item()

    @staticmethod
    def __display_menu():
        print("""
        1.键购买
        2.键结算
        """)

    def __select_menu_item(self):
        action = input("请输入选择：")
        if action == "1":
            self.__controller.buying()
        elif action == "2":
            self.__controller.settlement()


class ShoppingController:
    def __init__(self):
        self.__order = []

    @property
    def order(self):
        return self.__order

    @staticmethod
    def __print_commodity_info():
        for key, value in ShoppingModel.dict_commodity_info.items():
            print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))

    def buying(self):
        self.__print_commodity_info()
        self.__create_order()

    def __create_order(self):
        cid = int(input("请输入商品编号："))
        if cid not in ShoppingModel.dict_commodity_info:
            print("该商品不存在")
        count = int(input("请输入购买数量："))
        dict_order_info = {"cid": cid, "count": count}
        self.__order.append(dict_order_info)
        print("添加至购物车")

    def settlement(self):
        total_price = self.__calculate_total_price()
        self.__paying(total_price)

    def __calculate_total_price(self):
        total_price = 0
        for item in self.__order:
            commodity = ShoppingModel.dict_commodity_info[item["cid"]]
            total_price += commodity["price"] * item['count']
        return total_price

    def __paying(self, total_price):
        while True:
            money = float(input("总价%d元，请输入金额：" % total_price))
            if money >= total_price:
                print("购买成功，找回：%d元。" % (money - total_price))
                self.__order.clear()
                break
            else:
                print("金额不足.")


# 测试代码
# ShoppingView.print_commodity_info()
# ma = ShoppingController()
# ma.buying()
# print(ma.order)
view = ShoppingView()
view.shopping()
