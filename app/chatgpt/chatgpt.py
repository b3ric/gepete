import os
import openai


openai.organization = "org-5yY762ZV0aAg2rCUoD2sWQAq"
openai.api_key = os.getenv('OPENAI_API_KEY')


def chat_complete(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": f"{prompt}"},
        ],
        temperature=0.7,  
        max_tokens=1000  
    )

    return response

def img_gen(prompt):
    response = openai.Image.create(
        model="image-alpha-001",  
        prompt=f"{prompt}",  
        n=1,  
        size="512x512",
    )

    return response

def aud2text(f, lang):
    response = openai.Audio.transcribe(
        file = f,
        model='whisper-1',
        temperature = 0.7,
        language = lang
    )

    return response

# heitor/gouveia: aqui precisa de uma function p enviar um arquivo pra api da OpenAI
# similar as func acima