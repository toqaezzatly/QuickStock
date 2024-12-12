from flask import Flask, render_template, request, redirect, url_for, session
from models import Inventory
from auth import create_user, authenticate_user, login_required
from database import init_db

app = Flask(__name__)
app.secret_key = 'mysecretkey'

inventory = Inventory()

@app.route('/')
@login_required
def index():
    products = inventory.get_all_products()
    return render_template('index.html', inventory=products)


@app.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        inventory.add_product(name, price, quantity)
        return redirect(url_for('index'))
    return render_template('add_product.html')

@app.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = inventory.get_product(product_id)
    if not product:
        return "Product not found", 404
    if request.method == 'POST':
      name = request.form['name']
      price = float(request.form['price'])
      quantity = int(request.form['quantity'])
      inventory.update_product(product_id, name, price, quantity)
      return redirect(url_for('index'))
    return render_template('edit_product.html', product=product)

@app.route('/delete_product/<int:product_id>')
@login_required
def delete_product(product_id):
    inventory.delete_product(product_id)
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    user = authenticate_user(username, password)
    if user:
      session['user_id'] = user['id']
      return redirect(url_for('index'))
    else:
      return "Invalid username or password", 401
  return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if create_user(username, password):
      return redirect(url_for('login'))
    else:
      return "Username already exists", 409
  return render_template('register.html')

@app.route('/logout')
def logout():
  session.pop('user_id', None)
  return redirect(url_for('login'))

if __name__ == '__main__':
  app.run(debug=True)