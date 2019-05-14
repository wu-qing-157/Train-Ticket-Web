import pypinyin


def init():
    global station
    station_raw = open('station_list.txt', 'r').read().strip().split('\n')
    station = list(map(
        lambda s: tuple([s, ''.join(pypinyin.lazy_pinyin(s)), ''.join(map(lambda y: y[0], pypinyin.lazy_pinyin(s)))]),
        station_raw))


def match_chinese(keyword):
    ret_list = []
    num = 0
    for st in station:
        if st[0].startswith(keyword):
            ret_list.append(st[0])
            num += 1
            if num >= 5:
                break
    # keyword 为中文非前缀的一部分
    if num < 5:
        for st in station:
            if not st[0].startswith(keyword) and keyword in st[0]:
                ret_list.append(st[0])
                num += 1
                if num >= 5:
                    break
    return ret_list


def match_full(keyword):
    ret_list = []
    num = 0
    for st in station:
        if st[1] == keyword:
            ret_list.append(st[0])
            num += 1
            if num >= 5:
                break
    if num < 5:
        for st in station:
            if st[1] != keyword and st[1].startswith(keyword):
                ret_list.append(st[0])
                num += 1
                if num >= 5:
                    break
    return ret_list


def match_simple(keyword):
    ret_list = []
    num = 0
    for st in station:
        if st[2] == keyword:
            ret_list.append(st[0])
            num += 1
            if num >= 5:
                break
    if num < 5:
        for st in station:
            if st[2] != keyword and st[2].startswith(keyword):
                ret_list.append(st[0])
                num += 1
                if num >= 5:
                    break
    return ret_list


def match_level0(keyword):
    ret_list = []
    # keyword 为中文或其前缀
    num = 0
    for st in station:
        if st[0].startswith(keyword):
            ret_list.append(st[0])
            num += 1
            if num >= 10:
                break
    # keyword 为中文非前缀的一部分
    num = 0
    for st in station:
        if not st[0].startswith(keyword) and keyword in st[0]:
            ret_list.append(st[0])
            num += 1
            if num >= 5:
                break
    # keyword 为全拼
    num = 0
    for st in station:
        if st[1] == keyword:
            ret_list.append(st[0])
            num += 1
            if num >= 20:
                break
    # keyword 为简拼
    num = 0
    for st in station:
        if st[2] == keyword:
            ret_list.append(st[0])
            num += 1
            if num >= 20:
                break
    # keyword 为全拼前缀
    num = 0
    for st in station:
        if st[1] != keyword and st[1].startswith(keyword):
            ret_list.append(st[0])
            num += 1
            if num >= 5:
                break
    # keyword 为简拼前缀
    num = 0
    for st in station:
        if st[2] != keyword and st[2].startswith(keyword):
            ret_list.append(st[0])
            num += 1
            if num >= 10:
                break
    return ret_list


def match_level1(keyword):
    ret_list = []
    # keyword 为中文或其前缀
    num = 0
    for st in station:
        if st[0].startswith(keyword):
            ret_list.append(st[0])
            num += 1
            if num >= 10:
                break
    # keyword 为中文非前缀的一部分
    num = 0
    for st in station:
        if not st[0].startswith(keyword) and keyword in st[0]:
            ret_list.append(st[0])
            num += 1
            if num >= 5:
                break
    # keyword 为全拼
    num = 0
    for st in station:
        if st[1] == keyword:
            ret_list.append(st[0])
            num += 1
            if num >= 20:
                break
    # keyword 为简拼
    num = 0
    for st in station:
        if st[2] == keyword:
            ret_list.append(st[0])
            num += 1
            if num >= 20:
                break
    # keyword 为全拼前缀
    num = 0
    for st in station:
        if st[1] != keyword and st[1].startswith(keyword):
            ret_list.append(st[0])
            num += 1
            if num >= 5:
                break
    # keyword 为简拼前缀
    num = 0
    for st in station:
        if st[2] != keyword and st[2].startswith(keyword):
            ret_list.append(st[0])
            num += 1
            if num >= 10:
                break
    return ret_list