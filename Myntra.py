import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
# Search_results
    div --> a --> product details_page
    class="_2kHMtA" --> class="_1fQZEK" --> details_page
    class="_4ddWXP" --> class="_2rpwqI" --> details_page


    # For each product go to --> Product_details_page
        Name of product:                    span -> product_name
                                            class="B_NuCI"


        Price of product:                   div -> product_price
                                            class="_30jeq3 _16Jk6d"


        Overall rating of product:          div -> product_rating
                                            class="_3LWZlK"

        Reviews:                            div -> div -> div -> product_review
                                            class="t-ZTKy" -> div -> div

"""

def scrape_reviews_myntra(product_link):
    options = Options()
    options.add_argument('--headless')

    wbD = webdriver.Chrome(options=options)

    reviews = []
    # print(product_link)
    # Check if the product link is not None
    if product_link is not None or product_link != "":
        wbD.get(product_link)
        time.sleep(2)

        # Scrape the reviews
        review_elements = wbD.find_elements(by='xpath', value='//*[@class="user-review-reviewTextWrapper"]')
        for review_element in review_elements:
            review_text = review_element.text
            reviews.append(review_text)

    return reviews


def scrape_product_details_myntra(product_link):
    options = Options()
    options.add_argument('--headless')

    wbD = webdriver.Chrome(options=options)

    product_info = None

    if product_link is not None or product_link != "":
        wbD.get(product_link)
        time.sleep(2)

        #         Product info
        title_element = wbD.find_elements(by='xpath', value='.//h1[@class="pdp-title"]')
        name_element = wbD.find_elements(by='xpath', value='.//h1[@class="pdp-name"]')
        price_element = wbD.find_elements(by='xpath', value='.//span[@class="pdp-price"]')
        rating_element = wbD.find_elements(by='xpath', value='.//div[@class="index-overallRating"]/div[not(@class)]')
        # review_elements = wbD.find_elements(by='xpath', value='.//div[@class="user-review-reviewTextWrapper"]')

        review_collection = scrape_reviews_myntra(product_link)

        name = None
        price = None
        rating = None
        reviews = None

        if name_element:
            name = title_element[0].text + name_element[0].text
        if price_element:
            price = price_element[0].text
        if rating_element:
            rating = rating_element[0].text
        if len(review_collection) != 0:
            reviews = review_collection

        #         Create a dictionary for data info
        product_info = {
            "Name": name,
            "Price": price,
            "Rating": rating,
            "Reviews": reviews,
            "Product Link": product_link
        }

    return product_info


def web_scraping_myntra(link):
    options = Options()
    options.add_argument('--headless')

    web_driver = webdriver.Chrome(options=options)

    web_driver.get(link)
    time.sleep(5)
    related_products = []
    # //*[@data-component-type="s-search-result"]
    product_elements = web_driver.find_elements(by='xpath',
                                                value='//*[@class="results-base"]')
    print(product_elements)
#     for product in product_elements:
#         time.sleep(5)
#         # extract product detail link
#         product_detail_link = product.find_elements(by='xpath', value='(li/a[not(@class)])')
#
#         final_product_link = None
#         if len(product_detail_link) != 0:
#             final_product_link = product_detail_link[0].get_attribute('href')
#
#         # Now scrape the product details
#
#         if final_product_link is not None:
#             # Product info is in dictionary format which contains details about product
#             product_info = scrape_product_details_myntra(final_product_link)
#             related_products.append(product_info)
#
#     return related_products
#
#
key = input('Enter product to search: ')
link = 'https://www.myntra.com/' + key
#
products = web_scraping_myntra(link)
# # Save the data to a CSV file
# df = pd.DataFrame(products)
# df.to_csv('Myntra_Product_' + key + '.csv')
#
# print(products)
