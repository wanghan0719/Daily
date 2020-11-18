# 界面视图类：StudentManagerView
# 		数据：逻辑控制对象__manager
# 		行为：显示菜单__display_menu，选择菜单项__select_menu_item，入口逻辑main，
# 输入学生__input_students，输出学生__output_students，删除学生__delete_student，修改学生信息__modify_student
from 达内.Project.学生管理系统.bll import StudentManagerController


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
