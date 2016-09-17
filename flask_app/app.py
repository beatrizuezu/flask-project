from flask import Flask, render_template, abort

app = Flask(__name__)

PRODUCTS = {
    'iphone': {
        'name':'iPhone 5s',
        'category': 'Phones',
        'price': 699
    },
    'iphone': {
        'name':'iPhone 6s',
        'category': 'Phones',
        'price': 699
    },
    'iphone': {
        'name':'iPhone 7s',
        'category': 'Phones',
        'price': 699
    },
    'iphone': {
        'name':'iPhone 5c',
        'category': 'Phones',
        'price': 699
    }
}

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS)

@app.route('/produtos/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html',product=product)

if __name__ == '__main__':
    app.run()
