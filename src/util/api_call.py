import voyageai
from dotenv import load_dotenv
import os


def load_api_vars(): 
    load_dotenv()  # This loads the variables from .env
    VOYAGE_API_KEY = os.getenv('VOYAGE_API_KEY')
    client = voyageai.Client(api_key=VOYAGE_API_KEY)
    return client

def convert_statement(client, messages, max_tokens, model):
    print(f"Calling API with {model}")
    x = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        max_tokens=max_tokens,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return x

def get_response_text(response):
    return response.choices[0].message.content


def run_api_call(prompt, model, max_tokens = 7000):
    
    client = load_api_vars()
    response = convert_statement(client, prompt, max_tokens, model=model)
    content = get_response_text(response)
    return content 
