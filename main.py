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
        The assistant will initiate the conversation by asking the student for
        their name, email, and mobile\n
        It will ask what day the student will be arriving in the office and
        reply with whether Dr. Botazzi is available on that day.\n\n
        Ai:
        """
  
    # conversation with chatGPT
    text_message = ""

    while(text_message.lower()!="goodbye"): # conversation ends with a goodbye

        # get response from chatgpt
        response = generate_response(prompt) + "\nStudent:"
        print(response)
        prompt += response

        # get text input from student
        text_message = input()
        prompt += f"{text_message} \nAi:"
    
    
    # telling chatGPT to extract info from conversation
    conversation = prompt.split("day.\n\n")[1]

    INFO = ["name", "email", "mobile"]

    get_student_info_prompt = "Tell me the Student's {} from this conversation:\n\n" + conversation
 
    guest_name = generate_response(get_student_info_prompt.format(INFO[0]))
    guest_email = generate_response(get_student_info_prompt.format(INFO[1]))
    guest_mobile = generate_response(get_student_info_prompt.format(INFO[2]))

    print(guest_name, guest_email, guest_mobile)


if __name__ == "__main__":
  main()