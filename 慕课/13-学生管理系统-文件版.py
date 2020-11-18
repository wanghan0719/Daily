# 把功能代码抽取到函数的目的：提供功能代码的复用性，减少功能代码的冗余。
import os


# 学生列表，专门来负责管理每一个学生信息
student_list = []


# 显示学生管理系统菜单的功能函数
def show_menu():
    print("=================== 学生管理系统V1.0 ===================")
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 显示所有学生信息")
    print("6. 退出")


# 添加学生的功能函数
def add_student():
    # 实现添加学生的功能
    name = input("请输入的您的姓名:")
    age = input("请输入的您的年龄:")
    sex = input("请输入的您的性别:")
    # 每一个学生信息是字典类型，需要把这个三项数据组装到字典里面
    student_dict = {"name": name, "age": age, "sex": sex}
    # 把学生字典信息添加到列表
    student_list.append(student_dict)


# 显示所有学生的功能函数
def show_all_student():
    # 实现显示所有学生的功能
    for index, student_dict in enumerate(student_list):
        # 学号 = 下标 + 1
        student_no = index + 1
        print("学号: %d 姓名: %s 年龄: %s 性别: %s" % (student_no,
                                               student_dict["name"],
                                               student_dict["age"],
                                               student_dict["sex"]))


# 删除学生的功能函数
def remove_student():
    # 1. 接收要删除学生的学号
    student_no = int(input("请输入您要删除学生的学号:"))
    # 2. 根据学生生成下标
    index = student_no - 1
    # 判断下标是否合法
    if 0 <= index < len(student_list):
        # 3. 根据下标从列表中删除指定数据
        student_dict = student_list.pop(index)
        print("%s, 删除成功!" % student_dict["name"])
    else:
        print("请输入合法的学号!")


# 修改学生信息的功能函数
def modify_student():
    # 1. 接收要修改学生的学号
    student_no = int(input("请输入您要修改学生的学号:"))
    # 2. 根据学生生成下标
    index = student_no - 1
    # 判断下标是否合法
    if 0 <= index < len(student_list):
        # 3. 根据下标获取对应的学生字典信息
        modify_student_dict = student_list[index]
        # 4. 根据字典修改学生信息
        modify_student_dict["name"] = input("请输入您修改后的姓名:")
        modify_student_dict["age"] = input("请输入您修改后的年龄:")
        modify_student_dict["sex"] = input("请输入您修改后的性别:")
        print("修改成功")
    else:
        print("请输入您的合法学号！")


# 查询学生
def query_student():
    # 1. 接收用户入要查询学生的姓名
    name = input("请输入要查询学生的姓名:")
    # 2. 遍历学生列表，一次判断学生的姓名是否是指定名字
    for index, student_dict in enumerate(student_list):
        if student_dict["name"] == name:
            # 生成学生
            student_no = index + 1
            # 3. 如果找到了则输出学生信息，则停止循环
            print("学号: %d 姓名: %s 年龄: %s 性别: %s" % (student_no,
                                                   student_dict["name"],
                                                   student_dict["age"],
                                                   student_dict["sex"]))
            break
    else:
        # 4. 遍历完都没有找到，需要输出该用户不存在
        print("对不起，您查找的学生信息不存在！")


# 保存学生列表数据到文件
def save_data():
    print("student_list:", student_list)
    # 1. 打开文件
    file = open("student_list.data", "w", encoding="utf-8")
    # 2. 写入数据
    file.write(str(student_list))
    # 3. 关闭文件
    file.close()


# 加载文件中的数据到学生列表
def load_data():
    # 判断历史文件是否存在
    if os.path.exists("student_list.data"):
        # 读取文件中的数据，并把数据加载到学生列表里面
        # 1. 打开文件
        file = open("student_list.data", "r", encoding="utf-8")
        # 2. 读取文件中的数据
        content = file.read()
        # "[{'name': '张飞', 'age': '20', 'sex': '男'}, {'name': '刘备', 'age': '30', 'sex': '男'}]"
        # print(content, type(content))
        # 使用eval提取字符串里面包裹的列表数据
        new_list = eval(content)
        print(new_list, type(new_list))
        # 3. 读取数据后想办法把数据给学生列表
        student_list.extend(new_list)

        # 修改全局变量引用的写法
        # global student_list
        # student_list = new_list
        
        # 4. 关闭文件
        file.close()


# 学生管理系统的开发步骤
# 提示：由于系统需要一直运行，需要把以上三个步骤放到死循环里面，这样可以保存程序一直运行。
# 定义程序的入口函数，程序第一个要执行的函数
def start():
    # 加载历史文件中的数据，只加载1次即可
    load_data()
    while True:
        # 1. 显示学生管理系统的功能菜单
        show_menu()
        # 2. 接收用户输入的功能选项
        menu_option = input("请输入您要操作的功能选项:")
        # 3. 判断用户输入的功能选项，并完成相关的操作
        if menu_option == "1":
            print("添加学生")
            add_student()
        elif menu_option == "2":
            print("删除学生")
            remove_student()
        elif menu_option == "3":
            print("修改学生信息")
            modify_student()
        elif menu_option == "4":
            print("查询学生信息")
            query_student()
        elif menu_option == "5":
            print("显示所有学生信息")
            show_all_student()
        elif menu_option == "6":
            print("退出")
            # 保存数据到文件
            save_data()
            break


# 启动程序
start()




