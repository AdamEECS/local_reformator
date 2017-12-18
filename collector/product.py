from . import *


def get_product_1():
    url = url_base + 'Vote/get_product'
    data = {
        'type': '1',
        'start': '0',
        'limit': '100',
    }
    r = requests.post(url, data=data, headers=headers)
    r = r.content.decode(encoding='utf-8-sig')
    r = json.loads(r)
    rows = r['rows']
    print(len(rows))
    for product in rows:
        product['phase'] = 1
        p = Product.upsert(product)
        # print(p)


def get_product_2():
    url = url_base + 'Vote/get_product'
    data = {
        'type': '2',
        'start': '0',
        'limit': '100',
    }
    r = requests.post(url, data=data, headers=headers)
    r = r.content.decode(encoding='utf-8-sig')
    r = json.loads(r)
    rows = r['rows']
    print(len(rows))
    for product in rows:
        product['phase'] = 2
        p = Product.upsert(product)
        # print(p)


def get_product_3():
    url = url_base + 'Vote/get_product'
    data = {
        'type': '3',
        'start': '0',
        'limit': '110',
    }
    r = requests.post(url, data=data, headers=headers)
    r = r.content.decode(encoding='utf-8-sig')
    r = json.loads(r)
    rows = r['rows']
    print(len(rows))
    for product in rows:
        product['phase'] = 3
        p = Product.upsert(product)
        # print(p)

