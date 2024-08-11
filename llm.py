import os
from litellm import completion

# 在此处配置litellm的API KEY
# 如openai的api key
os.environ["OPENAI_API_KEY"] = "your-api-key"

def call_api(prompt):
    response = completion(
        model = "gpt-4o", 
        messages = [
            {"role": "system", "content": "You are an assisstant."},
            {"role": "user", "content": prompt},
        ],
    )
    response = response['choices'][0]['message']['content']
    return response
