import openai
from openai import OpenAI
from dotenv import load_dotenv
import os
import sys


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-3.5-turbo"
print(api_key)