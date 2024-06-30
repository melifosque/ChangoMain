from flask import Flask, render_template, request, redirect, url_for
from models import db, Customer, Order
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def init_db():
    with app.app_context():
        db.create_all()
        
@app.route('/')
def home():
    active_customers = Customer.query.filter_by(status='active').all()
    orders = Order.query.join(Customer).filter(Customer.status == 'active').all()
    return render_template('index.html', orders=orders, customers=active_customers)

@app.route('/orders')
def orders():
    orders = Order.query.all()
    return render_template('orders.html', orders=orders)

@app.route('/customers')
def customers():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']
        new_customer = Customer(name=name, status=status)
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for('customers'))
    return render_template('add_customer.html')

@app.route('/edit_customer/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    customer = Customer.query.get_or_404(id)
    if request.method == 'POST':
        customer.name = request.form['name']
        customer.status = request.form['status']
        db.session.commit()
        return redirect(url_for('customers'))
    return render_template('edit_customer.html', customer=customer)

@app.route('/delete_customer/<int:id>')
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('customers'))

@app.route('/add_order', methods=['GET', 'POST'])
def add_order():
    customers = Customer.query.all()
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        product = request.form['product']
        order_date = datetime.strptime(request.form['order_date'], '%Y-%m-%d')
        new_order = Order(customer_id=customer_id, product=product, order_date=order_date)
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('orders'))
    return render_template('add_order.html', customers=customers)

@app.route('/edit_order/<int:id>', methods=['GET', 'POST'])
def edit_order(id):
    order = Order.query.get_or_404(id)
    customers = Customer.query.all()
    if request.method == 'POST':
        order.customer_id = request.form['customer_id']
        order.product = request.form['product']
        order.order_date = datetime.strptime(request.form['order_date'], '%Y-%m-%d')
        db.session.commit()
        return redirect(url_for('orders'))
    return render_template('edit_order.html', order=order, customers=customers)

@app.route('/delete_order/<int:id>')
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for('orders'))

if __name__ == '__main__':
    app.run(debug=True)

