from openai import OpenAI
from ollama import Client, chat, ChatResponse

ollama_client = Client(host='0.0.0.0:11434')
omodel = 'llama2-uncensored'
client = OpenAI(
  api_key="your-api-key-here"
)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

gpt_text = response.choices[0].message.content
print("GPT Response:", gpt_text)


BadAiresponse = ollama_client.chat(
        model=omodel,
        keep_alive=0,
        messages=[{'role': 'system', 'content': f'You are a jaded internet troll and meme master remixing this poem: {gpt_text}. You have a way with words and swear and curse freely. Be creative and remix this to be nasty and rude and hostile while keeping the same structure. Be original. Use swear and curse words and explict terms innovatively- be the slim shady of ai: {gpt_text}'}]
    )
print("Ollama Response:", BadAiresponse['message']['content'])
