from collector import product


def task_all():
    product.get_product_1()
    product.get_product_2()
    product.get_product_3()


def task_daily():
    product.daily_task()


def main():
    task_daily()


if __name__ == '__main__':
    main()
