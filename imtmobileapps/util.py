import openai
import constants

openai.api_key = constants.OPENAI_API_KEY


# Comment
# Summaries include topics that are not related to the topic of focus.
# Delimiters can be anything like: ```, """, < >, <tag> </tag>, :

# A note about the backslash
# We are using a backslash \ to make the text fit on the screen
# without inserting newline '\n' characters.
# GPT-3 isn't really affected whether you insert newline characters or not.
# But when working with LLMs in general, you may consider whether newline characters
# in your prompt may affect the model's performance.


# This helper function will make it easier to use prompts and look at the generated outputs:


def get_completion(prompt_check, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt_check}]
    response_help = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response_help.choices[0].message["content"]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    #     print(str(response.choices[0].message))
    return response.choices[0].message["content"]


def user_messages(messages):
    global issue
    for issue in messages:
        prompt_translate_5 = f"Tell me what language this is: ```{issue}```"
        lang = get_completion(prompt_translate_5)
        print(f"Original message ({lang}): {issue}")

    prompt_translate_6 = f"""
    Translate the following  text to English \
    and Korean: ```{issue}```
    """

    response_messages = get_completion(prompt_translate_6)
    print(response_messages, "\n")

