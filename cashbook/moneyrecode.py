import os
import json
import time, pprint


# 周判断
def when_week(day):
    all_day = list(range(1, 32))
    if day in all_day[0:7]:
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


# 创建文件夹
def save_creat():
    where = os.getcwd()
    when = get_when_now()
    save_creat_path = where + '/files/{years}/{month}/'.format(years=when[0], month=when[3])
    if when[1] == 1:
        os.makedirs(save_creat_path, exist_ok=True)
    return save_creat_path


# 创建文件
def first(save_creat_path):
    now = get_when_now()
    save_creat_path_01 = save_creat_path + now[4]
    if now[5] == 0:
        os.system('touch ' + save_creat_path_01)
        with open(save_creat_path_01, 'w') as a:
            a.write(json.dumps([[0], [1], [2], [3], [4], [5], [6]]))
    return save_creat_path_01


# 主要信息部分
def main_recoder():
    a = time.localtime()
    time_now = str(a[0]) + str(a[1]) + str(a[2])
    print('~'*20)
    status = input('支出(+)或收入(-):')
    how_money = input('金额大小：')
    if status == '+':
        what_to_do = input('来源说明：')
    elif status == '-':
        what_to_do = input("使用说明：")
    else:
        what_to_do = 'None'
    how_to_do = input('来源或使用方式：')
    others = input('备注：')
    print('-'*20)
    all_in_tuple = (time_now, status, how_money, what_to_do, how_to_do, others)
    all_in_tuple_string = ['time_now', 'status', 'how_money', 'what_to_do', 'how_to_do', 'others']
    one_data = {}
    for i in range(len(all_in_tuple)):
        one_data.setdefault(all_in_tuple_string[i], all_in_tuple[i])
    return one_data


# 文件操作
def read_and_write(data, save_path):
    with open(save_path, 'r') as a:
        all_data = json.loads(a.read())
        pprint.pprint(all_data)
    with open(save_path, 'w') as a:
        week_status = time.localtime()[6]
        for i in all_data:
            if i[0] == week_status:
                i.append(data)
        a.write(json.dumps(all_data))


# 来咯～～～～
def main():
    save_creat_path = save_creat()
    save_creat_path_01 = first(save_creat_path=save_creat_path)
    one_data = main_recoder()
    read_and_write(save_path=save_creat_path_01, data=one_data)


if __name__ == '__main__':
    main()
