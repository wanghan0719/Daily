# 数据模型类：StudentModel
# 		数据：编号 id,姓名 name,年龄 age,成绩 score …
class StudentModel:
    """
    学生数据模型
    """

    def __init__(self, name="", age=0, score=0.0):
        self.id = 0  # 真实数据由添加学生时确定
        self.name = name
        self.age = age
        self.score = score
        __stu_list = []


# 逻辑控制类：StudentManagerController
# 		数据：学生列表 __stu_list
# 		行为：获取列表只读属性 stu_list,添加学生 add_student，删除学生remove_student，修改学生update_student，根据成绩排序order_by_score。
class StudentManagerController:
    """"
    学生管理控制器：主要负责处理程序的主要逻辑（算法）
    """
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []  # 创建学生列表

    @property
    def stu_list(self):
        return self.__stu_list  # 私有属性的访问方式

    @classmethod
    def __generate_id(cls):
        """
        id生成
        :return:
        """
        cls.__init_id += 1
        return cls.__init_id

    def add_student(self, stu_info):
        """
        添加学生，由界面获取学生信息方法调用
        :param stu_info:需要添加的学生对象（信息）
        :return:
        """
        pass
        stu_info.id = StudentManagerController.__generate_id()
        self.__stu_list.append(stu_info)

    def remove_student(self, stu_id):
        """
        删除学生，由界面获取学生信息方法调用
        :param stu_id:删除学生的ID
        :return:
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)
                return True  # 删除成功
        return False  # 删除失败
        pass

    def update_student(self, stu_info):
        """
        修改学生信息
        :param stu_info: 要修改的学生的信息
        :return:
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True  # 修改成功
        return False  # 修改失败

        pass

    def order_by_score(self):
        """
        根据成绩升序排序
        :return:
        """
        for i in range(len(self.__stu_list) - 1):
            for j in range(i + 1, len(self.__stu_list)):
                if self.__stu_list[i].score > self.__stu_list[j].score:
                    self.__stu_list[i], self.__stu_list[j] = self.__stu_list[j], self.__stu_list[i]

        pass


# 界面视图类：StudentManagerView
# 		数据：逻辑控制对象__manager
# 		行为：显示菜单__display_menu，选择菜单项__select_menu_item，入口逻辑main，
# 输入学生__input_students，输出学生__output_students，删除学生__delete_student，修改学生信息__modify_student
class StudentManagerView:
    def __init__(self):
        self.__manager = StudentManagerController()

    @staticmethod
    def __display_menu():
        """
        显示菜单项
        :return:
        """
        print(""""
        1)添加学生信息
        2)显示学生信息
        3）删除学生信息
        4）修改学生信息
        5）按照成绩从低到高显示
        """)

    def __select_menu_item(self):
        """
        选择菜单项
        :return:
        """
        action = input("请输入选项：")
        if action == "1":
            self.__input_students()  # 添加学生信息
        elif action == "2":
            self.__output_students()  # 显示学生信息
        elif action == "3":
            self.__delete_student()  # 删除学生信息
        elif action == "4":
            self.__modify_student()  # 修改学生信息
        elif action == "5":
            self.__out_student_by_score()  # 按照分数从低到高排序

    def main(self):
        """
        主程序
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def __input_students(self):
        while True:
            name = input("请输入学生姓名：")
            age = int(input("请输入学生年龄："))
            score = float(input("请输入学生成绩："))
            stu = StudentModel(name, age, score)
            self.__manager.add_student(stu)
            if input("输入Exit退出：") == "Exit":
                break

    def __output_students(self):
        for item in self.__manager.stu_list:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        stu_id = input("请输入要删除学生的id：")
        if self.__manager.remove_student(stu_id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.id = input("请输入要修改的学生id：")
        stu.name = input("请输入要修改的学生姓名：")
        stu.age = int(input("请输入要修改的学生年龄："))
        stu.score = input("请输入要修改的学生成绩：")
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __out_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_students()


view = StudentManagerView()
view.main()


