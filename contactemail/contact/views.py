from django.shortcuts import render
from django.core.mail import send_mail



def home (request):
    if request.method == "POST":
        message_name = request.POST.get('message_name')
        message_email = request.POST.get('message_email')
        message_subject = request.POST.get('message_subject')
        message = request.POST.get('message')

        send_mail(
            message_subject,
            'Name: '+ message_name + '\nEmail: ' + message_email + '\n' + message,
            'andrii.kom@ukr.net',
            ['andrii.kom@ukr.net', 'andrii.kom94@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'contact/index.html', {'message_name': message_name})

    else:
        return render(request, 'contact/index.html', { })
