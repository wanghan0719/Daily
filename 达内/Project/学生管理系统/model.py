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

