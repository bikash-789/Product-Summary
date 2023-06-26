from flask import Flask, render_template, request
from main import search_product

import sys

sys.path.append('../Web-Scraping/Client-Side')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/products', methods=["POST"])
def get_products():
    key = request.form['key']
    # key = 'sony camera'

    related_products = search_product(key)

    amazon = related_products['Amazon']
    # print("\n\n\n\n\n\n")
    # print(type(amazon[0]['Reviews'])) => list
    amz_ccat_reviews = ""
    for review in amazon[0]['Reviews']:
        amz_ccat_reviews = amz_ccat_reviews + review + "\n"
    amazon[0]['Reviews'] = amz_ccat_reviews

    # print(amazon[0]['Reviews'])
    # print("\n\n\n\n\n\n")

    summary = Summarize(amazon[0]['Reviews'])
    # print(amazon[0]['Reviews'])
    amazon[0]['Reviews'] = summary

    flipkart = related_products['Flipkart']
    # print(type(flipkart[0]['Reviews'])) => List
    fkt_ccat_reviews = ""
    for review in flipkart[0]['Reviews']:
        fkt_ccat_reviews = fkt_ccat_reviews + review + "\n"
    flipkart[0]['Reviews'] = fkt_ccat_reviews

    # print(flipkart[0]['Reviews'])
    # print("\n\n\n\n\n\n")

    summary = Summarize(flipkart[0]['Reviews'])
    # print(flipkart[0]['Reviews'])
    flipkart[0]['Reviews'] = summary

    # print("\n\n\n\n\n\n")
    # print(flipkart[0]['Reviews'])
    # print("\n\n\n\n\n\n")

    num_products = len(related_products)

    return render_template('response.html', amazon=amazon, flipkart=flipkart, num_products=num_products, key=key)


if __name__ == '__main__':
    app.run()
