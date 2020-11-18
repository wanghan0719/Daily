# WeekNamePrint.py
WeekStr = '星期一星期二星期三星期四星期五星期六星期日'
WeekId = eval(input("请输入星期数字（1-7）："))
pos = (WeekId-1)*3
print(WeekStr[pos:pos+3])