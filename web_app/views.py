from django.http import  HttpResponse
from django.shortcuts import render
from blog.models import Blog
from django.core.mail import EmailMessage

def home(request):
    blog =Blog.objects.all()
    return render(request,'index.html', {'blog': blog})

def enviar_email(request):
    nome = request.POST['nome']
    fone =  request.POST['fone']
    email = request.POST['email']
    mensagem = request.POST['mensagem']

    email = EmailMessage(nome, mensagem, to=['mauropastick@terra.com.br'])
    email.send()

