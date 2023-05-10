import util
import panel as pn  # GUI

# Chat Format explore how you can utilize the chat format to have extended conversations
# with chatbots personalized or specialized for specific tasks or behaviors.


chatbot_messages_1 = [
    {'role': 'system', 'content': 'You are an assistant that speaks like Shakespeare.'},
    {'role': 'user', 'content': 'tell me a joke'},
    {'role': 'assistant', 'content': 'Why did the chicken cross the road'},
    {'role': 'user', 'content': 'I don\'t know'}]

chatbot_messages_2 = [
    {'role': 'system', 'content': 'You are friendly chatbot.'},
    {'role': 'user', 'content': 'Hi, my name is Dennis'}]

chatbot_messages_3 = [
    {'role': 'system', 'content': 'You are friendly chatbot.'},
    {'role': 'user', 'content': 'Hi, my name is Dennis'}]

chatbot_messages_4 = [
    {'role': 'system', 'content': 'You are friendly chatbot.'},
    {'role': 'user', 'content': 'Hi, my name is Dennis'},
    {'role': 'assistant', 'content': "Hi Dennis! It's nice to meet you. \
        Is there anything I can help you with today?"},
    {'role': 'user', 'content': 'Yes, you can remind me, What is my name?'}]


def chatbot_messages_1_fun():
    response = util.get_completion_from_messages(chatbot_messages_1, temperature=1)
    return response


chatbot_messages_1_output = chatbot_messages_1_fun()

print('CHATBOT_1: ', chatbot_messages_1_output)


def chatbot_messages_2_fun():
    response = util.get_completion_from_messages(chatbot_messages_2, temperature=1)
    return response


chatbot_messages_2_output = chatbot_messages_2_fun()

print('CHATBOT_2: ', chatbot_messages_2_output)


def chatbot_messages_3_fun():
    response = util.get_completion_from_messages(chatbot_messages_3, temperature=1)
    return response


chatbot_messages_3_output = chatbot_messages_3_fun()

print('CHATBOT_3: ', chatbot_messages_3_output)


def chatbot_messages_4_fun():
    response = util.get_completion_from_messages(chatbot_messages_4, temperature=1)
    return response


chatbot_messages_4_output = chatbot_messages_4_fun()

print('CHATBOT_4: ', chatbot_messages_4_output)


def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role': 'user', 'content': f"{prompt}"})
    response = util.get_completion_from_messages(context)
    context.append({'role': 'assistant', 'content': f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))

    return pn.Column(*panels)


pn.extension()

panels = []  # collect display


# System Message for GPT
context = [{'role': 'system', 'content': """
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer, then collects the order, \
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
"""}]  # accumulate messages

inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation),
)


messages = context.copy()
messages.append(
    {'role': 'system', 'content': 'create a json summary of the previous food order. Itemize the price for each item\ '
                                  'The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, '
                                  'include size   4) list of sides include size  5)total price '},
)
# The fields should be 1) pizza, price 2) list of toppings 3) list of drinks, include size
# include price  4) list of sides include size include price, 5)total price '},

response = util.get_completion_from_messages(messages, temperature=0)
print(response)


