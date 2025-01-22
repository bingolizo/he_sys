from django.shortcuts import render
from django.core.mail import send_mail

def send_test_email(request):
    subject = 'Test Email from Django'
    message = 'Your appointment have been set.'
    from_email = 'lizobingo@gmail.com' 
    recipient_list = ['deufateka@gmail.com'] 

    send_mail(
        subject, message, from_email, recipient_list, fail_silently=False
    )

    return render(request, 'email_app/email_sent.html', {})  # Create an email_sent.html template
