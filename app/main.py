from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"status":"ok"}




client = OpenAI(
    api_key=os.environ.get("OPEN_API_KEY"),
)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)