from flask import render_template
from record_shop import record_shop
from models.records_4_sale import orders

@record_shop.route('/orders')
def index():
    return render_template('index.html', title='Home', orders=orders)

@record_shop.route('/orders/<order>')
def order():
    return render_template('order.html', title='Record Sold', order= f"{order}", orders=orders )

    #/orders/2
    #El Mar No Cesa by Heroes del Silencio"