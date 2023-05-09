import util
# Infer sentiment and topics from product reviews and news articles.


lamp_review = """
Needed a nice lamp for my bedroom, and this one had \
additional storage and not too high of a price point. \
Got it fast.  The string to our lamp broke during the \
transit and the company happily sent over a new one. \
Came within a few days as well. It was easy to put \
together.  I had a missing part, so I contacted their \
support and they ignored me! \
Another crucial piece was broken. \
I wasted my money on this piece of junk! \
Lumina seems to me to be a bogus company that does not care \
about their customers and products!!
"""

# Sentiment (positive/negative)
let_gpt_decide_prompt = f"""
What is the sentiment of the following product review, 
which is delimited with triple backticks?

Review text: '''{lamp_review}'''
"""

tell_gpt_how_prompt = f"""
What is the sentiment of the following product review, 
which is delimited with triple backticks?

Give your answer as a single word, either "positive" \
or "negative".

Review text: '''{lamp_review}'''
"""

# Identify types of emotions
identify_types_of_emotions_prompt = f"""
Identify a list of emotions that the writer of the \
following review is expressing. Include no more than \
five items in the list. Format your answer as a list of \
lower-case words separated by commas.

Review text: '''{lamp_review}'''
"""

# Identify anger
identify_anger_prompt = f"""
Is the writer of the following review expressing anger?\
The review is delimited with triple backticks. \
Give your answer as either yes or no.

Review text: '''{lamp_review}'''
"""

# Extract product and company name from customer reviews
extract_product_company_name_prompt = f"""
Identify the following items from the review text: 
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks. \
Format your response as a JSON object with \
"Item" and "Brand" as the keys. 
If the information isn't present, use "unknown" \
as the value.
Make your response as short as possible.
  
Review text: '''{lamp_review}'''
"""

# Doing multiple tasks at once
doing_multiple_tasks_prompt = f"""
Identify the following items from the review text: 
- Sentiment (positive or negative)
- Is the reviewer expressing anger? (true or false)
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks. \
Format your response as a JSON object with \
"Sentiment", "Anger", "Item" and "Brand" as the keys.
If the information isn't present, use "unknown" \
as the value.
Make your response as short as possible.
Format the Anger value as a boolean.

Review text: '''{lamp_review}'''
"""


def multiple_tasks():
    response = util.get_completion(doing_multiple_tasks_prompt)
    return response


# doing_multiple_tasks_prompt_output = multiple_tasks()
# print('MULTIPLE Tasks: ', doing_multiple_tasks_prompt_output)


def extract_product_company():
    response = util.get_completion(extract_product_company_name_prompt)
    return response


# extract_product_company_name_prompt_output = extract_product_company()
# print('EXTRACT ProductName and CompanyName: ', extract_product_company_name_prompt_output)


def identify_anger():
    response = util.get_completion(identify_anger_prompt)
    return response


# identify_anger_prompt_output = identify_anger()
# print('IDENTIFY ANGER: ', identify_anger_prompt_output)


def identify_emotions():
    response = util.get_completion(identify_types_of_emotions_prompt)
    return response


# identify_types_of_emotions_prompt_output = identify_emotions()

# print('IDENTIFY TYPES of EMOTIONS: ', identify_types_of_emotions_prompt_output)


def tell_gpt_how():
    response = util.get_completion(tell_gpt_how_prompt)
    return response


tell_gpt_how_prompt_output = tell_gpt_how()

print('TELL GPT how: ', tell_gpt_how_prompt_output)


def let_gpt_decide():
    response = util.get_completion(let_gpt_decide_prompt)
    return response


let_gpt_decide_output = let_gpt_decide()

print('GPT decided this: ', let_gpt_decide_output)

# Inferring topics
story = """
In a recent survey conducted by the government, 
public sector employees were asked to rate their level 
of satisfaction with the department they work at. 
The results revealed that NASA was the most popular 
department with a satisfaction rating of 95%.

One NASA employee, John Smith, commented on the findings, 
stating, "I'm not surprised that NASA came out on top. 
It's a great place to work with amazing people and 
incredible opportunities. I'm proud to be a part of 
such an innovative organization."

The results were also welcomed by NASA's management team, 
with Director Tom Johnson stating, "We are thrilled to 
hear that our employees are satisfied with their work at NASA. 
We have a talented and dedicated team who work tirelessly 
to achieve our goals, and it's fantastic to see that their 
hard work is paying off."

The survey also revealed that the 
Social Security Administration had the lowest satisfaction 
rating, with only 45% of employees indicating they were 
satisfied with their job. The government has pledged to 
address the concerns raised by employees in the survey and 
work towards improving job satisfaction across all departments.
"""

# Infer 5 topics
infer_5_topics_prompt = f"""
Determine five topics that are being discussed in the \
following text, which is delimited by triple backticks.

Make each item one or two words long. 

Format your response as a list of items separated by commas.

Text sample: '''{story}'''
"""


def infer_5_topics():
    response = util.get_completion(infer_5_topics_prompt)
    return response


infer_5_topics_prompt_output = infer_5_topics()
print('INFER 5 Topics: ', infer_5_topics_prompt_output)

topic_list = str(infer_5_topics_prompt_output).split(sep=',')
print('TOPIC LIST: ', topic_list)

# now put topic_list into a dictionary
topic_dict = {}
for i, topic in enumerate(topic_list):
    topic_dict[i] = topic

print('TOPIC DICT: ', topic_dict)

# Iterate Dictionary
# Use a regular expression to find the keywords in the value, ignoring whitespace and null values
# value = re.findall(r'\b\w+(?=\s|$)', value.strip())

# Iterate over the value and print the corresponding greeting
topic_value = infer_5_topics_prompt_output

for key, value in topic_dict.items():
    # print(f'The key is {key} and the value is {value}')
    my_value = str(value.strip().lower())
    if my_value is None:
        break
    if 'nasa' in my_value:
        print('HEY NASA!')
    elif 'social security' in my_value:
        print('HEY Social Security Administration!')
    elif 'employee' in my_value:
        print('HEY Employee Concerns!')
    elif 'job satisfaction' in my_value:
        print("HEY Job Satisfaction!")
    elif 'government' in my_value:
        print("HEY Government Survey!")
    else:
        print("Unknown")




