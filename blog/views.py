from django.shortcuts import render
from .models import Blog
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views import generic
from .forms import DadosEmailForm

# Create your views here.
def lista_blog():
    blog =Blog.objects.all()[:4]
    return blog


class EmailView(generic.FormView):
    template_name = 'index.html'
    form_class = DadosEmailForm

    def form_valid(self, form):
        ret_original = super().form_valid(form)

        email = form.cleaned_data.get('email')
        contexto = {
            'nome': form.cleaned_data.get('nome'),
            'telefone': form.cleaned_data.get('telefone'),
            'mensagem': form.cleaned_data.get('mensagem'),
        }

        conteudo_email = render_to_string('index.html', context=contexto)

        send_mail(
            subject='assunto do email',
            message=conteudo_email,
            from_email='remetente@examplo.com',
            recipient_list=[email, ],
            fail_silently=False,
            html_message=True
        )
        return ret_original