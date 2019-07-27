# 查看模块添加所有的源数据为一个变量(self.all_all)的格式
# 最外层是一个字典，这个字典最多有12个键：月
# 每一个月对应的值也是一个元组最多有5个键：firstweek, secondweek, thirdweek, fourthweek, fifthweek
# 每个键对应一个列表，每个列表包括7个列表，7个每个列表的第一个元素是range(0-7)，每个数字代表那一周的哪一天，7个列表的第二个元素起是一个字典
# 包括的每一个帐条的基本信息，包括时间，状态(收入还是支出)，用了多少，用来做什么，怎么用的，备注
example = {
    'january': {
        'firstweek': [],
        'secondweek': [],
        'thirdweek': [],
        'fourthweek': [],
        'fifthweek': []
    },
    'february': {
        'firstweek': [[0, {"time_now": "2019722", "status": "-", "how_money": "456", "what_to_do": "testing", "how_to_do": "testing", "others": "testing"}],
                  [1, {"time_now": "2019723", "status": "-", "how_money": "789", "what_to_do": "testing", "how_to_do": "testing", "others": "testing"},
                   {"time_now": "2019723", "status": "+", "how_money": "012", "what_to_do": "testing", "how_to_do": "testing", "others": "testing"},
                   {"time_now": "2019723", "status": "-", "how_money": "345", "what_to_do": "iii", "how_to_do": "ooo", "others": "ppp"}],
                  [2],
                  [3],
                  [4],
                  [5],
                  [6]],
        'secondweek': [],
        'thirdweek': [],
        'fourthweek': [],
        'fifthweek': []
    }
}


# 保存数据的源格式：
[[0, {"time_now": "2019722", "status": "-", "how_money": "456", "what_to_do": "testing", "how_to_do": "testing", "others": "testing"}],
                  [1, {"time_now": "2019723", "status": "-", "how_money": "789", "what_to_do": "testing", "how_to_do": "testing", "others": "testing"},
                   {"time_now": "2019723", "status": "+", "how_money": "012", "what_to_do": "testing", "how_to_do": "testing", "others": "testing"},
                   {"time_now": "2019723", "status": "-", "how_money": "345", "what_to_do": "iii", "how_to_do": "ooo", "others": "ppp"}],
                  [2],
                  [3],
                  [4],
                  [5],
                  [6]]




