from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.mail.message import EmailMessage

def mail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        data = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message
        }
        message = '''
        Username: {} 
        Message: {}
        From: {}
        '''.format(data['name'], data['message'], data['email'])
        send_mail(data['subject'], message, email, ['yolllllim@gmail.com'])
        return HttpResponse('Thank you for sending the mail.')
    return render(request, 'mail.html', {})

