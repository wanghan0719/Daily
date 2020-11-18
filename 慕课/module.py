
class Book:
    lang = "learn python with laoqi"

    def __init__(self, author):
        self.author = author

    def get_name(self):
        return self.author


def new_booK():
    return "数据准备和特征工程"


if __name__ == "__name__":
    python = Book("laoqi")
    author_name = python.get_name()
    print(author_name)  # laoqi
    published = new_booK()
    print(published)  # 数据准备和特征工程
