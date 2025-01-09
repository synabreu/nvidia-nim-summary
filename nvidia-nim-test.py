from openai import OpenAI
import os

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.getenv('NVIDIA_API_KEY')
)

completion = client.chat.completions.create(
  model="meta/llama-3.1-8b-instruct",
  messages=[{"role":"user","content":"who is Jensen Huang?"}],
  temperature=0.5,
  top_p=0.8,
  max_tokens=1024,
  stream=True
)

# API 응답이 여러 “청크”로 나뉘어 들어오므로, 각 청크를 순회하며 처리함.
for chunk in completion:
  if chunk.choices[0].delta.content is not None: # API 응답에서 현재 청크의 텍스트 내용 추출
    print(chunk.choices[0].delta.content, end="") # 출력된 텍스트를 화면에 표시하며, 줄바꿈 없이 이어서 출력(end="").
