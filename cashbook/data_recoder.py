import json
import os


# 查询object是否存在
def lookup(data_root, second, objects):
    return data_root[second].get(objects)


# second输入与检测
def second_input_inspect():
    while True:
        who = input('\n你需要添加的类型是什么[o/online_pay]|[b/bank_cards]:').lower().replace(' ', '')
        if who == 'o' or who == 'online_pay':
            return 'online_pay'
        elif who == 'b' or who == 'bank_cards':
            return 'bank_cards'
        else:
            print('输入错误')
            print('可以输入单个字母或全称[o/online_pay]|[b/bank_cards]')
            continue


# third输入与检测
def third_input_inspect(data_root, seconds):
    while True:
        already_have = []
        for i in data_root[seconds].keys():
            already_have.append(i)
        print('\n目前所有的名称: '+json.dumps(already_have))
        what = input('\n你需要添加的名称是什么：').lower().replace(' ', '')
        result = lookup(data_root=data_root, second=seconds, objects=what)
        if not result:
            data_root[seconds].setdefault(what, [])
            return what
        else:
            return what


# online_pay添加：
def add_online_pay(data_root, second, third):
    account = input('\n帐号：')
    password = input('密码:')
    pay_password = input('支付密码(可选)：')
    one = []
    one.append('account:'+account)
    one.append('password:'+password)
    one.append('pay_password:'+pay_password)
    data_root[second][third].append(one)


# bank_cards添加：
def add_bank_cards(data_root, second, third):
    print('\n进入银行卡添加系统!\n')
    types = input('类型：')
    numbers = input('卡号：')
    mobile_phone = input('绑定的手机号码：')
    one = []
    one.append('types:'+types)
    one.append('numbers:'+numbers)
    one.append('phone:'+mobile_phone)
    data_root[second][third].append(one)


# 更改
def change_systems(data_root, seconds, tagger):
    already_have = []
    for i in data_root[seconds].keys():
        already_have.append(i)
    print('\n目前拥有的项目: \n')
    for i in range(len(already_have)):
        print(str(i+1)+':'+already_have[i])
    who = input('\n更改的项目是(选择序号)：')
    for i in range(len(data_root[seconds][already_have[int(who)-1]])):
        print('\n'+str(i+1)+'.'+json.dumps(data_root[seconds][already_have[int(who)-1]][i]))
    who_01 = input('\n需要更改的是(选择序号):')
    for i in range(len(tagger)):
        print(str(i+1)+':'+tagger[i])
    who_02 = input('\n哪一项(选择序号)：')
    three = input('\n更改后：')
    data_root[seconds][already_have[int(who)-1]][int(who_01)-1][int(who_02)-1] = tagger[int(who_02)-1].lower()+':'+three


# 美化输出
def search_and_print(data_root, seconds):
    already_have = []
    for i in data_root[seconds].keys():
        already_have.append(i)
    print('\n目前拥有的项目: \n')
    for i in range(len(already_have)):
        print(str(i+1)+':'+already_have[i])
    who = input('\n查看的项目是(选择序号)：')
#    for i in range(len(data_root[seconds][already_have[int(who)-1]])):
#        print('\n'+str(i+1)+'.'+json.dumps(data_root[seconds][already_have[int(who)-1]][i]))
    for i in range(len(data_root[seconds][already_have[int(who)-1]])):
        print('-'*20)
        for j in data_root[seconds][already_have[int(who)-1]][i]:
            print(j)
        print('-'*20)
        print('\n')


# 统计
def count_account(data_root, seconds):
    all_account = 0
    a = {}
    what_third = data_root[seconds].keys()
    for i in what_third:
        a.setdefault(i, len(data_root[seconds][i]))
        all_account += len(data_root[seconds][i])
    return a, all_account


# 查看模块
def view(data_root):
    whats = input('你需要查看的类型是什么[o/online_pay]|[b/bank_cards]:').lower().replace(' ', '')
    if whats == 'o' or whats == 'online_pay':
        seconds = 'online_pay'
        account_dict, all_01 = count_account(data_root=data_root, seconds=seconds)
        print('\n目前，您的{seconds}共有{all}个帐号\n'.format(seconds=seconds, all=all_01))
        for i in account_dict:
            print('{i}有{count}个帐号'.format(i=i, count=account_dict[i]))
        search_and_print(data_root=data_root, seconds=seconds)
    elif whats == 'b' or whats == 'bank_cards':
        seconds = 'bank_cards'
        account_dict, all_01 = count_account(data_root=data_root, seconds=seconds)
        print('\n目前，您的{seconds}共有{all}个银行卡\n'.format(seconds=seconds, all=all_01))
        for i in account_dict:
            print('{i}有{count}个银行卡'.format(i=i, count=account_dict[i]))
        search_and_print(data_root=data_root, seconds=seconds)


# 更改模块
def change(data_root):
    online_pay_using = ['Account', 'Password', 'Pay_password']
    bank_cards_using = ['Types', 'Numbers', 'Mobile_phone']
    change_who = input('你需要更改的类型是什么[o/online_pay]|[b/bank_cards]:').lower().replace(' ', '')
    if change_who == 'online_pay' or change_who == 'o':
        change_who = 'online_pay'
        change_systems(data_root=data_root, seconds=change_who, tagger=online_pay_using)
    elif change_who == 'bank_cards' or change_who == 'b':
        change_who = 'bank_cards'
        change_systems(data_root=data_root, seconds=change_who, tagger=bank_cards_using)


# 添加模块
def add_01(data_root):
    second = second_input_inspect()
    third = third_input_inspect(data_root=data_root, seconds=second)
    if second == 'online_pay':
        add_online_pay(data_root=data_root, second=second, third=third)
    elif second == 'bank_cards':
        add_bank_cards(data_root=data_root,  second=second, third=third)


# 来咯～～～
def main():
    with open(os.getcwd() + '/files/data_root', 'r') as data:
        data_all = json.loads(data.read())
    while True:
        print('您可以进行以下操作：\n1.查看\n2.添加\n3.更改\n')
        what_to_do = input('进行的操作是(选择序号)：')
        if what_to_do == '1':
            view(data_root=data_all)
        elif what_to_do == '2':
            add_01(data_root=data_all)
        elif what_to_do == '3':
            change(data_root=data_all)
        want_to_do = input('\n是否继续操作[y\\n]:')
        if want_to_do == 'y':
            continue
        else:
            break
    with open(os.getcwd() + '/files/data_root', 'w') as data:
        data.write(json.dumps(data_all))


if __name__ == "__main__":
    main()
