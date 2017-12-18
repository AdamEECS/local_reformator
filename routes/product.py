from . import *
from models.product import Product

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
