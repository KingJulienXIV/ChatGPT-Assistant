import os
import openai


# personal api key goes here
with open(r"C:\Users\Marjet\Documents\HoloVision\api_key", "r") as f:
  openai.api_key = f.read()


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
    stop=[" Student:", " AI:"]
  )
  return response.choices[0].text


def main():
    prompt = """
        Dr. Vitor Botazzi is available on Tuesdays and Thursdays.
        The following is a conversation with an AI assistant. 
        The assistant is helpful, creative, clever, and very friendly.\n
        The assistant will try to get the student's name, email, and mobile\n\n
        AI: Hello I'm a chatbot assistant, how may I assist you today?\n
        Student:
        """
  
    # conversation with chatGPT
    text_message = ""

    while(text_message.lower()!="goodbye"): # conversation ends with a goodbye
        # get text input from student
        text_message = input()
        prompt += f"{text_message} \nAi:"

        # get response from chatgpt
        response = generate_response(prompt) + "\nStudent:"
        print(response)
        prompt += response
    
    
    # telling chatGPT to extract info from conversation
    INFO = ["name", "email", "mobile"]
    get_student_info_prompt = f"Extract the Student {INFO[0]} from this conversation:\n\n"


    get_student_info_prompt += prompt
    guest_name = generate_response(get_student_info_prompt)
    guest_email = generate_response(get_student_info_prompt)
    guest_mobile = generate_response(get_student_info_prompt)

    print(guest_name, guest_email, guest_mobile)


if __name__ == "__main__":
  main()