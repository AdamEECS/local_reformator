from collector import product, product_user


def task_all():
    product.get_product_1()
    product.get_product_2()
    product.get_product_3()


def task_daily():
    product.daily_task()


def task_product_user():
    product_user.get_product_user_all()


def main():
    task_daily()
    # task_all()
    # task_product_user()


if __name__ == '__main__':
    main()
