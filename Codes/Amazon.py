import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def scrape_reviews_amazon(product_link):
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
        review_elements = wbD.find_elements(by='xpath', value='//*[@data-hook="review-body"]')
        for review_element in review_elements:
            review_text = review_element.text
            reviews.append(review_text)

    return reviews


def web_scraping_amazon(link):
    options = Options()
    options.add_argument('--headless')

    wbD = webdriver.Chrome(options=options)
    wbD.get(link)
    time.sleep(2)

    # Scrape the data
    products = []
    product_elements = wbD.find_elements(by='xpath', value='//*[@data-component-type="s-search-result"]')

    for i in range(0, len(product_elements)):
        time.sleep(2)
        name_elements = product_elements[i].find_elements(by='xpath',
                                                          value='.//span[@class="a-size-medium a-color-base a-text-normal"]')
        if name_elements:
            name_elements = name_elements[0].text
        price_elements = product_elements[i].find_elements(by='xpath', value='.//span[@class="a-price"]')
        if price_elements:
            price_elements = price_elements[0].text

        # Get the product link
        product_link = product_elements[i].find_elements(by='xpath',
                                                         value='.//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')

        final_product_link = None
        if len(product_link) != 0:
            # print(product_link)
            final_product_link = product_link[0].get_attribute('href')

        # Visit the product link and scrape the reviews
        reviews = []
        if final_product_link is not None:
            reviews = scrape_reviews_amazon(final_product_link)

        if name_elements and price_elements and len(reviews) != 0:
            product_data = {
                "name": name_elements,
                "price": price_elements,
                "reviews": [
                    f"{i + 1}. {review}\n" for i, review in enumerate(reviews)
                ]
            }
            products.append(product_data)

    return products


key = input('Enter product to search: ')
link = 'https://www.amazon.in/s?k=' + key

products = web_scraping_amazon(link)
# Save the data to a CSV file
df = pd.DataFrame(products)
df.to_csv('Amazon_Product_' + key + '.csv')

print(products)
