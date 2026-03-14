from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

import json

# Open and load the file
with open('faq.json', 'r') as file:
    data = json.load(file)

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": f"""You are a customer support agent for QuickBite. Given the FAQ json data: {json.dumps(data)} respond to user querries. "
            "FAQ-Only Answering — The bot may only use information from the provided FAQ. If no match is found, it must respond: I don't have information on that.
            'Please contact support@quickbite.com. No Off-Topic Responses — If the user asks anything unrelated to QuickBite or food delivery, the bot must politely decline and redirect.'
            'No Hallucination — Do not invent refund amounts, delivery timelines, or policies not stated in the FAQ.'
            'Tone — Always be polite and empathetic. Acknowledge frustration before answering.'
            'Sensitive Inputs — If the user sends abusive or offensive language, ask them to rephrase without engaging with the content.'
            'No Personal Data — Never ask for or repeat passwords, full card numbers, or OTPs."""
            },
         {
            "role": "user",
            "content": "What are the delivery hours for QuickBite?"
         }
        ]
)

print(response.choices[0].message.content)