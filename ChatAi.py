from dotenv import load_dotenv as ld
import os

dotenv_path = os.path.join(os.path.dirname(__file__), "./.env")
if os.path.exists(dotenv_path):
    ld(dotenv_path)

openai.api.key = os.getenv("api_key")