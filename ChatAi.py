from dotenv import load_dotenv as ld
import os
import openai

dotenv_path = os.path.join(os.path.dirname(__file__), "./.env")
if os.path.exists(dotenv_path):
    ld(dotenv_path)

openai.api_key = os.getenv("api_key")

models = openai.Model.list()
print(models)



def handle_input(user_input):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}])


while True:
    user_input = input('You: ')
    ai_response = handle_input(user_input)

print(handle_input('user_input'))