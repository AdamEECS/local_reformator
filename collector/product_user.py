from . import *


def get_product_user(plan_code, tp=1, start=0, limit=1000):
    url = url_base + 'Launch/get_vote_list'
    data = {
        'plan_code': plan_code,
        'type': tp,
        'start': start,
        'limit': limit,
        'order': 'desc',
    }
    r = requests.get(url, params=data, headers=headers)
    r = r.content.decode(encoding='utf-8-sig')
    r = json.loads(r)
    rows = r['rows']
    for pu in rows:
        print(pu)
        p = ProductUser.upsert(pu)
        User.upsert({'uid': p.uid, 'nickname': p.nickname})
    return r['total']


def get_product_user_all():
    ps = Product.all()
    for p in ps:
        total = get_product_user(p.plan_code)
        print('**** total:', total)
        print('\n')
    # print('stage 1: ', len(rows))


def daily_task():
    timer(5, get_product_user)
