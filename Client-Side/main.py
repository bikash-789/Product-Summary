from Amazon import web_scraping_amazon
from Flipkart import web_scraping_flipkart

import openai


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.25,
    )
    return response.choices[0].message["content"]


def Summarize(content):
    # _ = load_dotenv(find_dotenv())
    openai.api_key = ''

    prod_review = content

    prompt = f"""
    Your task is to generate a short summary of a product \
    review from an ecommerce site to give overall idea \
    about the product to the new customer.

    Summarize the review below, delimited by triple
    backticks, in at most 150 words, and focusing on quality of\
    the product, the good and bad in terms of price and satisfaction \
    level. Do consider if the customer had any issue in the delivery \
    and customer service. Finally also state the bads of the product \
    as well. Also include line breaks where necessay in the response.

    Review: ```{prod_review}```
    """

    response = get_completion(prompt)
    return response


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
