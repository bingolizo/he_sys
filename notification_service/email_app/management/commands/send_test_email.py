from django.core.management.base import BaseCommand
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Send a test email'

    def handle(self, *args, **options):
        subject = 'Test Email from Django'
        message = 'your appointment have been set.'
        from_email = 'lizobingo@gmail.com' 
        recipient_list = ['deufateka@gmail.com'] 

        send_mail(
            subject, message, from_email, recipient_list, fail_silently=False
        )
        self.stdout.write(self.style.SUCCESS('Test email sent!'))