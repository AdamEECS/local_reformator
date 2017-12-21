import time


def time_str(t):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(int(t) + 3600 * 8))


def time_gmt_str(t):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(int(t)))


def time_str_datetime(t):
    return time.strftime("%Y-%m-%dT%H:%M", time.gmtime(int(t) + 3600 * 8))


def role(r):
    d = {
        '1': '发起人',
        '2': '管理人',
        '3': '跟投人',
    }
    return d[str(r)]


def role2(r):
    d = {
        '0': '',
        '1': '[联合]',
    }
    return d[str(r)]


def phase(r):
    d = {
        '1': '募集中',
        '2': '运营中',
        '3': '已清盘',
    }
    return d[str(r)]


filters = {
    'time_str': time_str,
    'time_str_datetime': time_str_datetime,
    'time_gmt_str': time_gmt_str,
    'role': role,
    'role2': role2,
    'phase': phase,
}
