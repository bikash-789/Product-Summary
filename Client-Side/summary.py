import openai
import os

# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())


openai.api_key = ''

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.25,
    )
    return response.choices[0].message["content"]


x = ["I recently purchased the Apple Watch SE GPS 44mm in the Starlight Aluminium Case with Starlight Sport Band, and I must say, it has exceeded my expectations in every way. This smartwatch has quickly become an integral part of my daily life, offering a seamless blend of functionality, style, and convenience.\n\nFirst and foremost, the performance of the Apple Watch SE is truly impressive. The built-in GPS allows for accurate tracking of my outdoor activities, whether it's running, hiking, or cycling. The heart rate monitor and the various workout features help me stay motivated and reach my fitness goals. The watch's water resistance is a great bonus, as it can be worn during swimming sessions without any worries.\n\nThe watchOS operating system is smooth and intuitive, providing a user-friendly experience. The Retina display is vibrant, crisp, and easy to read, even under direct sunlight. Navigating through apps and notifications is a breeze thanks to the responsive touch screen and the well-designed interface.\n\nOne of the standout features of the Apple Watch SE is its extensive ecosystem of apps and customizable watch faces. There is an app for nearly everything, from productivity tools and health trackers to entertainment and social media platforms. The ability to personalize the watch face with various complications allows me to have all the information I need at a glance.\n\nThe build quality and design of the watch are impeccable. The Starlight Aluminium Case adds a touch of elegance and durability, while the Starlight Sport Band is comfortable to wear for extended periods. The watch fits perfectly on my wrist, and I appreciate the option to switch bands easily, allowing me to match my watch to any occasion.\n\nBattery life is impressive considering the watch's capabilities. With moderate use, I can easily go a full day without needing to recharge. However, it's worth noting that more intensive usage, such as extended workouts with GPS tracking, may require more frequent charging.\n\nThe seamless integration with my iPhone is another standout feature. I can receive and respond to messages, make calls, and control music playback right from my wrist. The ability to stream music and podcasts directly to the watch without needing my phone is a game-changer during workouts or when I want to enjoy a walk without carrying my phone.\n\nIn conclusion, the Apple Watch SE GPS 44mm in the Starlight Aluminium Case with Starlight Sport Band is an outstanding smartwatch that delivers on both style and functionality. Its performance, user-friendly interface, and extensive app ecosystem make it an invaluable companion for fitness enthusiasts, professionals, and tech-savvy individuals alike. If you're in the market for a reliable and feature-packed smartwatch, look no further than the Apple Watch SE. Highly recommended!\n\nPros:\n\nAffordable Entry into the Apple Watch Ecosystem: The Apple Watch SE offers a fantastic way to experience the Apple Watch features without breaking the bank. It provides exceptional value for its price point.\nSleek Design: The Starlight Aluminum Case with the matching Sport Band gives the Apple Watch SE a premium and stylish appearance. It seamlessly blends with any outfit, whether casual or formal.\nPerfect Size and Comfort: The 44mm size strikes a great balance between a prominent display and a comfortable fit on the wrist. The lightweight aluminium case combined with the Starlight Sport Band makes it easy to wear all day without discomfort.\nImpressive Display: The Retina OLED display of the Apple Watch SE is vibrant, sharp, and easy to read, even in bright sunlight. The touch responsiveness is excellent, ensuring a smooth and seamless user experience.\nComprehensive Fitness Tracking: With advanced sensors and an accurate heart rate monitor, the Apple Watch SE helps you track various fitness metrics like steps, calories burned, workouts, and even sleep quality. It encourages an active lifestyle and motivates you to achieve your fitness goals.\nSeamless Integration with Apple Ecosystem: Being an Apple product, the Watch SE seamlessly syncs with your iPhone, providing access to a wide range of apps, notifications, and the ability to respond to messages directly from your wrist. It offers a convenient and efficient way to stay connected.\n\nCons:\n\nNo Always-On Display: Unlike the higher-end Apple Watch models, the SE does not have an always-on display feature. While the screen wakes up quickly with a wrist raise, some users may miss the constant visibility of the time and notifications without needing to raise their wrist.\nLimited Health Features: The Apple Watch SE lacks some of the advanced health features found in the more expensive models, such as the ECG app and blood oxygen level monitoring. However, it still offers an impressive array of fitness tracking capabilities.\nBattery Life Could Be Better: The battery life of the Apple Watch SE is decent but not exceptional. With typical usage, you'll need to charge it every day or every other day, which may be a minor inconvenience for some users.", 'I had series-3 (2018 purchase) and now wanted to switch to SE version. I loved it. Bigger screen and improved features than pervious one…. Thank you ifamily.', 'Good product', 'It’s obviously a wow factor', 'Loved this product! I’m getting close to 2 days battery time which I did not expect from an apple watch! The OS is very well optimised or maybe it’s the new S8 chip, but everything is super smooth! Unfortunately, the glass scratches so easily :/\n\nOn the second day, I accidentally touched a concrete wall, and I got 2 scratches! I suggest you to get a good case for it! My iPhone 13 has no screen protection and is still scratch free after being exposed to a lot of similar accidents.\n\nApart from this, I’d say go for it. As an entry level smart watch into the Apple eco system, it does its job very well.', 'I’m still charging it, 30mins passed. Man, this is disappointing. Will update if it’s start working\n\nEdit: after two hours of plugging in, it finally woke up. It is as good as it gets. It’s frickin awesome', 'Apple is Apple', 'Watch is good, backup is 1.5 day with max features off']
# content = ""
# for c in x:
#     content = content + c + "\n"

prod_review = x

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
print(response)
