from . import *


def get_product(tp=1, start=0, limit=100):
    url = url_base + 'Vote/get_product'
    data = {
        'type': tp,
        'start': start,
        'limit': limit,
    }
    r = requests.post(url, data=data, headers=headers)
    r = r.content.decode(encoding='utf-8-sig')
    r = json.loads(r)
    rows = r['rows']
    return rows


def get_product_1():
    rows = get_product(1)
    print('stage 1: ', len(rows))
    for product in rows:
        product['phase'] = 1
        Product.upsert(product)


def get_product_2():
    rows = get_product(2)
    print('stage 2: ', len(rows))
    for product in rows:
        product['phase'] = 2
        Product.upsert(product)


def get_product_3():
    rows = get_product(3)
    print('stage 3: ', len(rows))
    for product in rows:
        product['phase'] = 3
        Product.upsert(product)


def manager_monitor():
    rows = get_product(1)
    print(time_str(timestamp()), '侦测到敌机数量：', len(rows))
    for product in rows:
        product['phase'] = 1
        p = Product.upsert(product)
        if p.manager_uid == 68:
            alarm.play()
            # pyglet.app.run()


def daily_task():
    timer(5, manager_monitor)
