from openai import OpenAI
import os
import httpx
httpx_client=httpx.Client(verify=False)

api_key = "xxxxxxxx"
base_url = "https://az.gptplus5.com/v1"
path = "qwq-plus"
question = "你好"

client = OpenAI(
    http_client=httpx_client,
    api_key=api_key,
    base_url=base_url
)

completion = client.chat.completions.create(model=path, messages=[{'role': 'user', 'content': question}], stream=True, stream_options={"include_usage": True})

def stream_content(completion):
    reasoning_content = ""
    content = ""
    for chunk in completion:
        delta = chunk.choices[0].delta
        if hasattr(delta, 'reasoning_content') and delta.reasoning_content is not None:
            reasoning_content += delta.reasoning_content
        else:
            if delta.content:
                content += delta.content
    return reasoning_content, content

reasoning_content, content = stream_content(completion)
print(content)
