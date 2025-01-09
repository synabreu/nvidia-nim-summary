import openai 

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[{"role":"user","content":"who is Jensen Huang?"}],
  temperature=0.5,
  top_p=0.8,
  max_tokens=1024,
  stream=True
)

# API 응답이 여러 “청크”로 나뉘어 들어오므로, 각 청크를 순회하며 처리함.
for chunk in response:
    if "choices" in chunk and chunk["choices"][0]["delta"].get("content"):
        print(chunk["choices"][0]["delta"]["content"], end="")