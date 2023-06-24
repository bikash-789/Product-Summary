from flask import Flask, render_template, request, jsonify
from main import search_product
from rq import Queue
from redis import Redis
import time

import sys

sys.path.append('../Web-Scraping/Client-Side')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/products', methods=["POST"])
def get_products():
    key = request.form['key']
    related_products = search_product(key)
    amazon = related_products['Amazon']
    flipkart = related_products['Flipkart']
    num_products = len(related_products)
    return render_template('response.html', amazon=amazon, flipkart=flipkart, num_products=num_products, key=key)


if __name__ == '__main__':
    app.run()
