from django.core.mail import EmailMessage, send_mass_mail
from django.shortcuts import render

from Home.models import Contato
from .models import Mensagem


def enviar_mensagem(request):
    if request.method == 'POST':
        mensagem = Mensagem.objects.first()
        assunto = request.POST.get('assunto')
        corpo = request.POST.get('corpo')
        anexo = request.FILES.get('anexo')

        contatos = Contato.objects.values_list('email', flat=True)

        mensagem = Mensagem(
            assunto=mensagem,
            corpo=corpo,
            anexo=anexo
        )

        email = EmailMessage(
            assunto,
            corpo,
            'seuemail@gmail.com',
            contatos
        )

        if anexo:
            email.attach(anexo.name, anexo.read(), anexo.content_type)

        email.send()

        mensagem.save()

        return render(request, 'enviar_mensagem.html', {'sucesso': True})

    return render(request, 'enviar_mensagem.html')
