from flask import Flask, render_template, request
from main import search_product, Summarize

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

    amz_ccat_reviews = ""
    for review in amazon[0]['Reviews']:
        amz_ccat_reviews = amz_ccat_reviews + review + "\n"
    amazon[0]['Reviews'] = amz_ccat_reviews
    summary = Summarize(amazon[0]['Reviews'])

    amazon[0]['Reviews'] = summary

    flipkart = related_products['Flipkart']

    fkt_ccat_reviews = ""
    for review in flipkart[0]['Reviews']:
        fkt_ccat_reviews = fkt_ccat_reviews + review + "\n"

    flipkart[0]['Reviews'] = fkt_ccat_reviews

    summary = Summarize(flipkart[0]['Reviews'])
    flipkart[0]['Reviews'] = summary

    num_products = len(related_products)

    return render_template('response.html', amazon=amazon, flipkart=flipkart, num_products=num_products, key=key)


if __name__ == '__main__':
    app.run()
