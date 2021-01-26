from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'contact/index.html')


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']

        send_mail(
            message_name,
            message_subject,
            message,
            message_email,
            ['andrii.kom@ukr.net'],
        )

        return render(request, 'index.html', {'message_name': message_name})

    else:
        return render(request, 'index.html', { })
