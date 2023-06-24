from Amazon import web_scraping_amazon
from Flipkart import web_scraping_flipkart


def search_product(key):
    amazon_link = 'https://www.amazon.in/s?k=' + key
    flipkart_link = 'https://www.flipkart.com/search?q=' + key
    amazon_products = web_scraping_amazon(amazon_link)
    flipkart_products = web_scraping_flipkart(flipkart_link)
    products = {
        'Amazon': amazon_products,
        'Flipkart': flipkart_products
    }
    return products
