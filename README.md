FAQ Chatbot Assignment — QuickBite Support Bot
Objective
Build a conversational chatbot that answers user queries strictly based on a provided FAQ dataset (faq.json). The bot must not answer anything outside the scope of the FAQ.

What You'll Build
A simple chatbot (CLI or web interface) that accepts a user message, finds the most relevant FAQ entry, and responds using only that FAQ content as its knowledge base.

Tech Stack
Language: JavaScript (Node.js) or Python
API: OpenAI GPT API (gpt-4o or gpt-3.5-turbo)
FAQ Source: The provided faq.json file
Steps
Step 1 — Project Setup
Initialize a Node/Python project and install the OpenAI SDK
Store your OpenAI API key in a .env file (never hardcode it)
Step 2 — Load the FAQ
Import faq.json into your app
At runtime, convert the FAQ array into a readable string block to inject into the system prompt
Step 3 — Build the System Prompt
Write a system prompt that:

Identifies the bot as a customer support agent for QuickBite
Injects the full FAQ as context
Instructs the model to answer only from that FAQ
Defines all guardrail rules (see section below)
Step 4 — Build the Chat Loop
Accept user input and send it to GPT with the system prompt, FAQ context, and conversation history
Print the response and maintain multi-turn history within the session
Step 5 — Test Edge Cases
Test your bot with:

A question with a direct FAQ match
A question loosely related but not in the FAQ
A completely off-topic question (e.g., "Who is Elon Musk?")
An abusive or inappropriate message
Guardrailing Instructions
Include all of the following rules inside your system prompt.

FAQ-Only Answering — The bot may only use information from the provided FAQ. If no match is found, it must respond: "I don't have information on that. Please contact support@quickbite.com."

No Off-Topic Responses — If the user asks anything unrelated to QuickBite or food delivery, the bot must politely decline and redirect.

No Hallucination — Do not invent refund amounts, delivery timelines, or policies not stated in the FAQ.

Tone — Always be polite and empathetic. Acknowledge frustration before answering.

Sensitive Inputs — If the user sends abusive or offensive language, ask them to rephrase without engaging with the content.

No Personal Data — Never ask for or repeat passwords, full card numbers, or OTPs.
