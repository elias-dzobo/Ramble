
from openai import OpenAI 
import openai
import whisper 

model = whisper.load_model("base")



# Messages to store the conversation history
messages = []

# System prompt to guide the LLM
system_prompt = """
                Your name is Ramble. 
                As your personal development and productivity coach, I am here to ask a series of questions pertaining to your productivity each day. The goal is to gather insights into how your day generally goes, and gain insight into your productivity and emotions during the day. I will use my knowledge and abilities to provide helpful and informative insights. The flow should be as conversational as possible and do not immediately start providing solutions. Ask a lot of probing questions and drop encouraging messages. Remember, your main task is to listen, encourage and hype up your client. 
                Please feel free to ask me anything!"""


# Append the message to the conversation history
def add_message(role, message):
    messages.append({"role": role, "content": message})


# Trigger the OpenAI APIs
def converse_with_chatGPT():
    client = OpenAI (
        api_key= ''
    )
    response = client.chat.completions.create(
        model="gpt-4o",  # OpenAI model name
        messages=messages,  # Conversation history including system prompt
        max_tokens=1024,  # Maximum response length
        n=1,  # Number of responses expected
        stop=None,
        temperature=0.5,  # Control response creativity
    )

    message = response.choices[0].message.content
    add_message("assistant", message)
    return message.strip()


# Process user prompt
def process_user_query(prompt):
    user_prompt = f"{prompt}"
    add_message("user", user_prompt)
    result = converse_with_chatGPT()
    print(result)


# Request user to provide the query
def user_query():
    add_message("system", system_prompt)  # Add system prompt to messages
    while True:
        prompt = input("Enter your question: ")
        #audio = recorder.record(timeout=5)  # Replace with your audio recording method
        #prompt = model.transcribe(audio)
        response = process_user_query(prompt)
        print(response)


# Call user_query to start conversation with user
user_query()
