import os
import time
import json


# 周判断
# 运行的逻辑是：判断日期，每7天作为一个周，每个月最多分出5个月，并且根据日所在的范围，判断是哪个周并且返回
def when_week(day):
    all_day = list(range(1, 32))
    if day in all_day[0: 7]:
        return 'firstweek'
    elif day in all_day[7:14]:
        return 'secondweek'
    elif day in all_day[14:21]:
        return 'thirdweek'
    elif day in all_day[21:28]:
        return 'fourthweek'
    elif day in all_day[28:]:
        return 'fifthweek'


# 月
# 非常简单的一个函数，根据月对应的索引，返回月的英文版本，不再是数字
def when_month(month):
    month_int = list(range(1, 12))
    month_eng = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                 'september', 'october', 'november', 'december']
    for i in zip(month_int, month_eng):
        if month == i[0]:
            return i[1]


# 获取目前具体时间
# 用来获取一些在一下判断使用到的信息，使用了time模块的localtime的函数
# 返回的元组依次是(年, 月(int)， 日(int), 月的字符串版本(调用了when_month函数), 周(调用了when_week函数)， 周所在日的标志)
def get_when_now():
    when_now = time.localtime()
    day = when_now[2]
    month = when_now[1]
    week = when_week(day=day)
    month_string = when_month(month=month)
    return when_now[0], month, day, month_string, week, when_now[6]


# path
# 用来创建保存数据的path
# 返回数据保存的路径(根据目前的月来创建)和get_when_now()的返回信息组
def where_path():
    now = get_when_now()
    w = "{basic}/files/{years}/{month}/".format(basic=os.getcwd(), years=now[0], month=now[3])
    return w, now


# 文本初始化
# 执行的步骤：
# 1. 先使用os模块的makedirs函数创建文件保存的路径(调用了where_path)路径
# 2. 根据周(信息组获取)创建数据保存的文件(如果按照这样的思维，每次创建文件都会覆盖原来创建文件的数据，但是这是一个初始化的作用，只执行一次，可以忽略)
# 3. 创建个人信息的文件
# 4. 分别初始化个人信息文件和数据保存的文件
def text_init():
    where, now = where_path()
    os.makedirs(where, exist_ok=True)
    os.system('touch ' + where + now[4])
    os.system('touch ' + "{basic}/files/data_root".format(basic=os.getcwd()))
    with open(where + now[4], 'w') as a:
        a.write(json.dumps([[0], [1], [2], [3], [4], [5], [6]]))
    with open("{basic}/files/data_root".format(basic=os.getcwd()), 'w') as a:
        a.write(json.dumps({'bank_cards': {}, 'online_pay': {}}))


if __name__ == '__main__':
    text_init()
