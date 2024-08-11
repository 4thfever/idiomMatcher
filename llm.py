import os
from litellm import completion

# 在此处配置litellm的API KEY
# 如openai的api key
os.environ["OPENAI_API_KEY"] = "your-api-key"
model = "gpt-4o"

# 支持其他类型的大模型api，如deepseek
os.environ['DEEPSEEK_API_KEY'] = "your-api-key"
model = "deepseek/deepseek-chat"

# 查询litellm的官网，检索更多支持的大模型API，如通义千问
# https://docs.litellm.ai/docs/providers

def call_api(prompt):
    response = completion(
        model = model, 
        messages = [
            {"role": "system", "content": "You are an assisstant."},
            {"role": "user", "content": prompt},
        ],
    )
    response = response['choices'][0]['message']['content']
    return response
