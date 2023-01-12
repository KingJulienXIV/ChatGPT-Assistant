import os
import openai

# personal api key goes here
with open(r"C:\Users\Marjet\Documents\HoloVision\api_key", "r") as f:
  openai.api_key = f.read()

prompt = """
  Dr. Vitor Botazzi is available on Tuesdays and Thursdays.
  The following is a conversation with an AI assistant. 
  The assistant is helpful, creative, clever, and very friendly.\n\n
  Human: Hello, who are you?\n
  AI: I am an AI created by OpenAI. How can I help you today?\n
  Human: I'd like to know when Dr. Botazzi is available.\n
  AI:
  """

def generate_response(prompt: str) -> str:
  """ Generates response to given prompt
  Code sourced from openai chat example
  """
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )
  return response.choices[0].text