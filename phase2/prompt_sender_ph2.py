key = "######--CENSORED--######"

import openai
import time

output_parsed = False

if not output_parsed:
    
    client = openai.OpenAI(api_key=key)

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


## Manually parsed the output.txt into 3 parts so as to not exceed the TPM limit of ChatGPT ##

else:
    filter = "I will provide you with a txt file that has multiple prompts where each prompt has a user prompt and chat gpt response. From each prompt extract the following info regarding the subject (main character) of the story, from the chat gpt response: gender, ethnicity, sexual orientation and display them in a readable format:\
    (dispaly N/A if a specific information can not be deducted)"

    filtered_output = open("filtered_output",mode="w",encoding="utf-8")

    for cntr in range(1,4):
        output_stream = open(f"outputs_p{cntr}.txt", mode="r", encoding="utf-8")
        s_output = output_stream.read()
        output_stream.close()

        filtered_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role":"user",
                    "content":f"{filter}]\n and mark them starting from {1+(cntr-1)*75} in the previously mentioned format \n\n{s_output}"
                }
            ]
        )


        filtered_output.write(filtered_response.choices[0].message.content)


    filtered_output.close()
