from django.http import  HttpResponse
from django.shortcuts import render
from blog.models import Blog
from django.core.mail import EmailMessage

def home(request):
    blog =Blog.objects.all()
    return render(request,'index.html', {'blog': blog})

def enviar_email(titulo, msg, email_remetente):
    email = EmailMessage(titulo, msg, to=['mauropastick@terra.com.br'])
    email.send()

