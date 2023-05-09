import util

# Transforming : Explore how to use Large Language Models for text transformation tasks such as language translation,
# spelling and grammar checking, tone adjustment, and format conversion.


# Translation

prompt_translate_1 = f"""
Translate the following English text to Spanish: \ 
```Hi, I would like to order a blender```
"""

prompt_translate_2 = f"""
Tell me which language this is: 
'Combien coûte le lampadaire?'
"""

prompt_translate_3 = f"""
Translate the following  text to French and Spanish
and English: \
'I want to order a basketball'
"""

prompt_translate_4 = f"""
Translate the following text to Spanish in both the \
formal and informal forms: 
'Would you like to order a pillow?'
"""

# Universal Translator

user_messages = [
    "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal
    "Mi monitor tiene píxeles que no se iluminan.",  # My monitor has pixels that are not lighting
    "Il mio mouse non funziona",  # My mouse is not working
    "Mój klawisz Ctrl jest zepsuty",  # My keyboard has a broken control key
    "我的屏幕在闪烁"  # My screen is flashing
]

# Tone Transformation

prompt_tone_transformation = f"""
Translate the following from slang to a business letter: 
'Dude, This is Joe, check out this spec on this standing lamp.'
"""

# Format Conversion
# ChatGPT can translate between formats. The prompt should describe the input and output formats.
data_json = {"restaurant employees": [
    {"name": "Shyam", "email": "shyamjaiswal@gmail.com"},
    {"name": "Bob", "email": "bob32@gmail.com"},
    {"name": "Jai", "email": "jai87@gmail.com"}
]}

prompt_format_conversion = f"""
Translate the following python dictionary from JSON to an HTML \
table with 2 columns named 'name' and 'email': {data_json}
"""

# Spellcheck/Grammar check.
# To signal to the LLM that you want it to proofread your text,
# you instruct the model to 'proofread' or 'proofread and correct'.

text_spell_check = [
    "The girl with the black and whit pupies have a ball.",  # The girl has a ball.
    "Yolanda has her noteook.",  # notebook
    "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
    "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
    "Your going to need you’re notebook.",  # Homonyms
    "That medicine effects my ability to sleep. Have you heard of the buterfly affect?",  # Homonyms
    "This phrase is to cherck chatGPT for speling abilitty"  # spelling
]

for t in text_spell_check:
    prompt_spell = f"""Proofread and correct the following text
    and rewrite the corrected version. If you don't find
    and errors, just say "No errors found". Don't use 
    any punctuation around the text but display as a JSON Object with the keys original and corrected:
    ```{t}```"""
    response = util.get_completion(prompt_spell)
    print(response)


text_spell_check_2 = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""
prompt_sp_2 = f"proofread and correct this review: ```{text_spell_check_2}```"
response_sp_2 = util.get_completion(prompt_sp_2)
print('PROOFREAD: ', response_sp_2)


def format_conversion():
    response_format = util.get_completion(prompt_format_conversion)
    return response_format


prompt_format_conversion_output = format_conversion()


def tone_trans():
    response_tone = util.get_completion(prompt_tone_transformation)
    return response_tone


prompt_tone_transformation_output = tone_trans()


def translate_four():
    response_trans_4 = util.get_completion(prompt_translate_4)
    return response_trans_4


prompt_translate_4_output = translate_four()


def translate_three():
    response_trans_3 = util.get_completion(prompt_translate_3)
    return response_trans_3


prompt_translate_3_output = translate_three()


def translate_one():
    response_trans_1 = util.get_completion(prompt_translate_1)
    return response_trans_1


prompt_translate_1_output = translate_one()


def translate_two():
    response_trans_2 = util.get_completion(prompt_translate_2)
    return response_trans_2


prompt_translate_2_output = translate_two()

print('TRANSLATE ONE: ', prompt_translate_1_output)
print('TRANSLATE TWO: ', prompt_translate_2_output)
print('TRANSLATE THREE: ', prompt_translate_3_output)
print('TRANSLATE FOUR: ', prompt_translate_4_output)
print('TONE TRANSFORMATION: ', prompt_tone_transformation_output)
print('FORMAT CONVERSION: ', prompt_format_conversion_output)

util.user_messages(user_messages)
