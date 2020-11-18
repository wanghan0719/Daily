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
