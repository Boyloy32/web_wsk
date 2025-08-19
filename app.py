from flask import Flask, render_template

app = Flask(__name__)

products = [
  {
    "id": 1,
    "title": "Zinvo Blade Dragon",
    "price": 430,
    "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    "category": "men's clothing",
    "image": "/static/pic/p1.jpg",
    "rating": {
      "rate": 3.9,
      "count": 120
    }
  },
  {
    "id": 2,
    "title": "Zinvo Blade Women White Magic ",
    "price": 390,
    "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
    "category": "men's clothing",
    "image": "/static/pic/p2.jpg",
    "rating": {
      "rate": 4.1,
      "count": 259
    }
  },
  {
    "id": 3,
    "title": "D1 MILANO UTBL32 ULTRA THIN BRACELET 30 MM - ULTIMATE GREY",
    "price": 395,
    "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.",
    "category": "men's clothing",
    "image": "/static/pic/p3.jpg",
    "rating": {
      "rate": 4.7,
      "count": 500
    }
  },
  {
    "id": 4,
    "title": "D1 MILANO UTBL33 ULTRA THIN BRACELET 30 MM - ASTRAL",
    "price": 395,
    "description": "The color could be slightly different between on the screen and in practice. / Please note that body builds vary by person, therefore, detailed size information should be reviewed below on the product description.",
    "category": "men's clothing",
    "image": "/static/pic/p4.jpg",
    "rating": {
      "rate": 2.1,
      "count": 430
    }
  },
  {
    "id": 5,
    "title": "Zinvo Rival 12",
    "price": 695,
    "description": "From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.",
    "category": "jewelery",
    "image": "/static/pic/p5.jpg",
    "rating": {
      "rate": 4.6,
      "count": 400
    }
  },
  {
    "id": 6,
    "title": "D1 MILANO UTBL30 ULTRA THIN BRACELET 30 MM - ZEPHYR GREY ",
    "price": 375,
    "description": "Satisfaction Guaranteed. Return or exchange any order within 30 days.Designed and sold by Hafeez Center in the United States. Satisfaction Guaranteed. Return or exchange any order within 30 days.",
    "category": "jewelery",
    "image": "/static/pic/p6.jpg",
    "rating": {
      "rate": 3.9,
      "count": 70
    }
  },
  {
    "id": 7,
    "title": "D1 MILANO UTBL34 ULTRA THIN BRACELET 30 MM - EDGE",
    "price": 450,
    "description": "Classic Created Wedding Engagement Solitaire Diamond Promise Ring for Her. Gifts to spoil your love more for Engagement, Wedding, Anniversary, Valentine's Day...",
    "category": "jewelery",
    "image": "/static/pic/p7.jpg",
    "rating": {
      "rate": 3,
      "count": 400
    }
  },
  {
    "id": 8,
    "title": "Zinvo Blade Volt Gem",
    "price": 410,
    "description": "Rose Gold Plated Double Flared Tunnel Plug Earrings. Made of 316L Stainless Steel",
    "category": "jewelery",
    "image": "/static/pic/p8.jpg",
    "rating": {
      "rate": 1.9,
      "count": 100
    }
  },
]

@app.get('/')
@app.get('/Home')
def home():
    return render_template('front/home.html', products=products)
@app.get('/product')
def product():
    return render_template('front/product.html', products=products)
@app.get('/cart')
def card():
    return render_template('front/cart.html')

@app.get('/checkout')
def checkout():
    return render_template('front/checkout.html')

@app.get('/vue')
def vue():
    return render_template('front/vue.html')


if __name__ == '__main__':
    app.run()
