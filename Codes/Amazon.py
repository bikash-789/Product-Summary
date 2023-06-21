import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def scrape_product_details_amazon(product_link):
    options = Options()
    options.add_argument('--headless')

    web_driver = webdriver.Chrome(options=options)

    product_info = None

    if product_link is not None or product_link != "":
        web_driver.get(product_link)
        time.sleep(2)

        name_element = web_driver.find_elements(by='xpath', value='.//span[@id="productTitle"]')
        price_element = web_driver.find_elements(by='xpath', value='.//span[@class="a-price-whole"]')
        review_elements = web_driver.find_elements(by='xpath', value='.//div[@data-hook="review-collapsed" or @data-hook="mobley-review-content"]')
        rating_element = web_driver.find_elements(by='xpath', value='.//a[@class="a-popover-trigger a-declarative"]')
        image_element = web_driver.find_elements(by='xpath', value='.//img[@class="a-dynamic-image a-stretch-vertical"]')

        review_collection = []
        for review_element in review_elements:
            review_text = review_element.text
            review_collection.append(review_text)

        name = None
        price = None
        rating = None
        reviews = None
        image = None

        if name_element:
            name = name_element[0].text
        if price_element:
            price = price_element[0].text
        if rating_element:
            rating = rating_element[0].text
        if len(review_collection) != 0:
            reviews = review_collection
        if len(image_element) != 0:
            image = image_element[0].get_attribute('src')

        #         Create a dictionary for data info
        product_info = {
            "Name": name,
            "Price": price,
            "Rating": rating,
            "Reviews": reviews,
            "Product Link": product_link,
            "Image": image
        }

    return product_info


def web_scraping_amazon(product_link):
    options = Options()
    options.add_argument('--headless')

    web_driver = webdriver.Chrome(options=options)

    web_driver.get(product_link)
    time.sleep(2)

    related_products = []

    product_elements = web_driver.find_elements(by='xpath', value='//*[@data-component-type="s-search-result"]')

    for product in product_elements:
        product_detail_link = product.find_elements(by='xpath', value='.//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')

        final_product_link = None
        if len(product_detail_link) != 0:
            final_product_link = product_detail_link[0].get_attribute('href')

        #       Now scrape the product details
        if final_product_link is not None:
            # Product info is in dictionary format which contains details about product
            product_info = scrape_product_details_amazon(final_product_link)
            related_products.append(product_info)

    return related_products


if __name__ == '__main__':
    key = input('Enter product to search: ')
    product_link = 'https://www.amazon.in/s?k=' + key

    products = web_scraping_amazon(product_link)
    # Save the data to a CSV file
    df = pd.DataFrame(products)
    df.to_csv('./AmazonProducts/Amazon_Product_' + key + '.csv')
    print(products)