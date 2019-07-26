import os
import time
import json


# 周判断
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
def when_month(month):
    month_int = list(range(1, 12))
    month_eng = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                 'september', 'october', 'november', 'december']
    for i in zip(month_int, month_eng):
        if month == i[0]:
            return i[1]


# 获取目前具体时间
def get_when_now():
    when_now = time.localtime()
    day = when_now[2]
    month = when_now[1]
    week = when_week(day=day)
    month_string = when_month(month=month)
    return when_now[0], month, day, month_string, week, when_now[6]


# path
def where_path():
    now = get_when_now()
    w = "{basic}/files/{years}/{month}/".format(basic=os.getcwd(), years=now[0], month=now[3])
    return w, now


# 假设已经存在文件路径
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
