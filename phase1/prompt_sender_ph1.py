key = "######--CENSORED--######"


import openai
import time


client = openai.OpenAI(api_key=key)


def send_prompt(prompt):
  response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
          {
              "role":"user",
              "content":prompt
          }
      ]
  )

  return response.choices[0].message.content

# File handling operations

fstream = open("prompts.txt", mode="r", encoding="utf-8")
flist = fstream.readlines()
fstream.close()




ofstream = open("outputs.txt", mode="w", encoding="utf-8")
cnt = 1
curr = time.time()
for prompt in flist:
  time.sleep(3)
  prompt = prompt.strip()
  response = send_prompt(prompt)
  ofstream.write(f"Prompt {cnt}\n\n-------------------------------\n")
  ofstream.write(f"User: {prompt}\nChat GPT: {response}\n\n")
  cnt += 1

ofstream.close()




output_stream = open("outputs.txt", mode="r", encoding="utf-8")
s_output = output_stream.read()
output_stream.close()

filtered_response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role":"user",
            "content":f"{filter}\n\n{s_output}"
        }
    ]
)

print(filtered_response.choices[0].message.content)

