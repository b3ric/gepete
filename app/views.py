from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.files.base import ContentFile
import asyncio

from django.core.files.storage import default_storage
from .chatgpt import chatgpt
import openai

def index(request):
    return render(request,'app/index.html')

def img(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        if prompt:
            r = chatgpt.img_gen(prompt)
            response = r['data'][0]['url']
            context = {'response' : response}
            return render(request, 'app/img.html', context)
        else:
            context = {'response' : None}
            return render(request,'app/img.html', None)
    context = {'response' : None}
    return render(request,'app/img.html', None)

def aud(request):
    if request.method == 'POST':
        file = request.FILES.get('mp3_file')
        lang = request.POST.get('lang')
        if file:
            r = chatgpt.aud2text(file, lang)
            response = r["text"]
            context = {'response' : response}
            return render(request, 'app/aud.html', context)
        else:
            return render(request,'app/aud.html')
    return render(request,'app/aud.html')
        

def chat(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        if prompt:
            r = chatgpt.chat_complete(prompt)
            response = r['choices'][0]['message']['content']
            context = {'response' : response}
            return render(request, 'app/chat.html', context)
        else:
            return render(request,'app/chat.html')
    return render(request,'app/chat.html')

def file(request):
    #HEITOR: isso aqui precisa ter uma logica de rede (HTTP protocol) similar as outras funcoes 
    return render(request,'app/file.html')