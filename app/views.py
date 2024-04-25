from django.shortcuts import render
from .chatgpt import chatgpt

def index(request):
    return render(request,'app/index.html')

def img(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        if prompt:
            res = chatgpt.img_gen(prompt)
            response = res['data'][0]['url']
            context = {'response' : response}
            return render(request, 'app/img.html', context)
        context = {'response' : None}
        return render(request,'app/img.html', None)
    context = {'response' : None}
    return render(request,'app/img.html', None)

def aud(request):
    if request.method == 'POST':
        aud_file = request.FILES.get('mp3_file')
        lang = request.POST.get('lang')
        if aud_file:
            res = chatgpt.aud2text(aud_file, lang)
            response = res["text"]
            context = {'response' : response}
            return render(request, 'app/aud.html', context)
        return render(request,'app/aud.html')
    return render(request,'app/aud.html')


def chat(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        if prompt:
            res = chatgpt.chat_complete(prompt)
            response = res['choices'][0]['message']['content']
            context = {'response' : response}
            return render(request, 'app/chat.html', context)
        return render(request,'app/chat.html')
    return render(request,'app/chat.html')

def file():
    # implementation pending
    pass
