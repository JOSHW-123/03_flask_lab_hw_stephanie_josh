from app import app
from flask import render_template
from classes.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders=orders)

@app.route('/orders/<index>')
def item(index):
    found_order = [int(float(index))]
