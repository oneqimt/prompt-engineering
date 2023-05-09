import util

# review for panda plush toy
review_1 = """
Got this panda plush toy for my daughter's birthday, \
who loves it and takes it everywhere. It's soft and \
super cute, and its face has a friendly look. It's \
a bit small for what I paid though. I think there \
might be other options that are bigger for the \
same price. It arrived a day earlier than expected, \
so I got to play with it myself before I gave it \
to her.
"""

# Summarize with a word/sentence/character limit
sum_word_sentence_prompt = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site. 

Summarize the review below, delimited by triple 
backticks, in at most 30 words. 

Review: ```{review_1}```
"""

# Summarize with a focus on shipping and delivery
sum_shipping_delivery_prompt = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site to give feedback to the \
Shipping department. 

Summarize the review below, delimited by triple 
backticks, in at most 30 words, and focusing on any aspects \
that mention shipping and delivery of the product. 

Review: ```{review_1}```
"""


def summarize_word_sentence():
    response_word = util.get_completion(sum_word_sentence_prompt)
    return response_word


sum_word_sentence_prompt_output = summarize_word_sentence()

print('WORD_SENTENCE_SUM: ', sum_word_sentence_prompt_output)


def summarize_shipping_delivery():
    response_ship = util.get_completion(sum_shipping_delivery_prompt)
    return response_ship


sum_shipping_delivery_prompt_output = summarize_shipping_delivery()

print('SHIPPING_DELIVERY_SUM: ', sum_shipping_delivery_prompt_output)

# Summarize with a focus on price and value


sum_price_value_prompt = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site to give feedback to the \
pricing department, responsible for determining the \
price of the product.  

Summarize the review below, delimited by triple 
backticks, in at most 30 words, and focusing on any aspects \
that are relevant to the price and perceived value. 

Review: ```{review_1}```
"""


def summarize_price_value():
    response_price = util.get_completion(sum_price_value_prompt)
    return response_price


sum_price_value_prompt_output = summarize_price_value()

print('PRICE_VALUE_SUM: ', sum_price_value_prompt_output)

# Try "extract" instead of "summarize"

extract_relevant_info_prompt = f"""
Your task is to extract relevant information from \ 
a product review from an ecommerce site to give \
feedback to the Shipping department. 

From the review below, delimited by triple quotes \
extract the information relevant to shipping and \ 
delivery. Limit to 30 words. 

Review: ```{review_1}```
"""


def extract_relevant_info():
    response_extract = util.get_completion(extract_relevant_info_prompt)
    return response_extract


extract_relevant_info_prompt_output = extract_relevant_info()

print('EXTRACT RELEVANT_INFO: ', extract_relevant_info_prompt_output)

# review for a standing lamp
review_2 = """
Needed a nice lamp for my bedroom, and this one \
had additional storage and not too high of a price \
point. Got it fast - arrived in 2 days. The string \
to the lamp broke during the transit and the company \
happily sent over a new one. Came within a few days \
as well. It was easy to put together. Then I had a \
missing part, so I contacted their support and they \
very quickly got me the missing piece! Seems to me \
to be a great company that cares about their customers \
and products. 
"""

# review for an electric toothbrush
review_3 = """
My dental hygienist recommended an electric toothbrush, \
which is why I got this. The battery life seems to be \
pretty impressive so far. After initial charging and \
leaving the charger plugged in for the first week to \
condition the battery, I've unplugged the charger and \
been using it for twice daily brushing for the last \
3 weeks all on the same charge. But the toothbrush head \
is too small. I’ve seen baby toothbrushes bigger than \
this one. I wish the head was bigger with different \
length bristles to get between teeth better because \
this one does not.  Overall if you can get this one \
around the $50 mark, it's a good deal. The manufacture's \
replacements heads are pretty expensive, but you can \
get generic ones that are more reasonably priced. This \
toothbrush makes me feel like I've been to the dentist \
every day. My teeth feel sparkly clean! 
"""

# review for a blender
review_4 = """
So, they still had the 17 piece system on seasonal \
sale for around $49 in the month of November, about \
half off, but for some reason (call it price gouging) \
around the second week of December the prices all went \
up to about anywhere from between $70-$89 for the same \
system. And the 11 piece system went up around $10 or \
so in price also from the earlier sale price of $29. \
So it looks okay, but if you look at the base, the part \
where the blade locks into place does not look as good \
as in previous editions from a few years ago, but I \
plan to be very gentle with it (example, I crush \
very hard items like beans, ice, rice, etc. in the \ 
blender first then pulverize them in the serving size \
I want in the blender then switch to the whipping \
blade for a finer flour, and use the cross cutting blade \
first when making smoothies, then use the flat blade \
if I need them finer/less pulpy). Special tip when making \
smoothies, finely cut and freeze the fruits and \
vegetables (if using spinach-lightly stew soften the \ 
spinach then freeze until ready for use-and if making \
sorbet, use a small to medium sized food processor) \ 
that you plan to use that way you can avoid adding so \
much ice if at all-when making your smoothie. \
After about a year, the motor was making a funny noise. \
I called customer service but the warranty expired \
already, so I had to buy another one. FYI: The overall \
quality has gone done in these types of products, so \
they are kind of counting on brand recognition and \
consumer loyalty to maintain sales. Got it in about \
two days.
"""


# Summarize multiple product reviews
reviews = [review_1, review_2, review_3, review_4]


for i in range(len(reviews)):
    prompt = f"""
    Your task is to generate a short summary of a product \ 
    review from an ecommerce site. 

    Summarize the review below, delimited by triple \
    backticks in at most 20 words. 

    Review: ```{reviews[i]}```
    """

    response = util.get_completion(prompt)
    number_of_words = len(response.split())
    print('SUMMARIZE MULTIPLE: ', i+1, response, "\n")
    print('The number of words are : ' + str(number_of_words))
