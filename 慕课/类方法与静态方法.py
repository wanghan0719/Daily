class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        print("当前输入的为{}年{}月{}日".format(self.year,self.month,self.day))

    @classmethod
    def from_str(cls, date_str):
        year, month, day = map(int, date_str.split('-'))
        date1 = cls(year, month, day)
        return date1

    @staticmethod
    def date_validate(date_str):
        year, month, day = map(int, date_str.split('-'))
        return year <= 2038 and month <= 12 and day <= 31


b = Date.from_str("2020-8-12")
is_date = Date.date_validate("2020-8-12")
print(b ,'\n',is_date)
