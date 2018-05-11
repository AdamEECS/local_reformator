from . import *
from models.product import Product
from models.product_user import ProductUser

main = Blueprint('product', __name__)


@main.route('/<int:phase>')
def index(phase):
    u = current_user()
    ps = Product.find(phase=phase)
    d = {
        1: 'product/1.html',
        2: 'product/2.html',
        3: 'product/3.html',
    }
    for p in ps:
        if phase == 1:
            continue
        a = float(p.EQUITY)
        b = p.launch_money
        t = 1
        if phase == 2:
            start = datetime.strptime(p.operation_start, '%Y-%m-%d %H:%M:%S')
            now = datetime.now()
            t = (now - start).days
        elif phase == 3:
            t = int(p.actual_operation)
        if t == 0:
            t = 1
        profit = (a - b) / b * 100
        profit_year = profit / int(p.operation_time) * 360
        # profit = '{:.2f}%'.format(profit)
        # profit_year = '{:.2f}%'.format(profit_year)
        p.profit = round(profit, 2)
        p.profit_year = round(profit_year, 2)
        p.t = t
        p.lt = int(p.operation_time) - t
    return render_template(d[phase], u=u, ps=ps)


@main.route('/mine')
def mine():
    u = current_user()
    pus = ProductUser.find(nickname='mccmccmcc')
    ps = []
    for pu in pus:
        p = Product.find_one(plan_code=pu.plan_code)
        p.my_in = pu.investor_capital_total_init
        p.my_out = pu.investor_capital_total
        p.my_profit = p.my_out - p.my_in
        ps.append(p)
    for p in ps:
        if p.phase == 1:
            continue
        a = float(p.EQUITY)
        b = p.launch_money
        t = 1
        if p.phase == 2:
            start = datetime.strptime(p.operation_start, '%Y-%m-%d %H:%M:%S')
            now = datetime.now()
            t = (now - start).days
        elif p.phase == 3:
            t = int(p.actual_operation)
        if t == 0:
            t = 1
        profit = (a - b) / b * 100
        profit_year = profit / int(p.operation_time) * 360
        # profit = '{:.2f}%'.format(profit)
        # profit_year = '{:.2f}%'.format(profit_year)
        p.profit = round(profit, 2)
        p.profit_year = round(profit_year, 2)
        p.t = t
        p.lt = int(p.operation_time) - t
    if u is None:
        u = User.find_one(nickname='mccmccmcc')
    u.all_profit = sum([p.my_profit for p in ps])
    return render_template('product/mine.html', u=u, ps=ps)


@main.route('/d/<code>')
def detail(code):
    p = Product.find_one(plan_code=code)
    pu = ProductUser.find(plan_code=code)
    return render_template('product_user.html', p=p, pu=pu)
