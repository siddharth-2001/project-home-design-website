from django.core.mail import send_mail
from .models import Appointment
from django.template.loader import render_to_string

def notify_email(phone):
    
    client = Appointment.objects.get(phone = phone)
    body1 = render_to_string('mail-template.html', context={'client' : client})
    body = 'A new user has booked an appointment. \nDetails: \nName: '+ client.name + ' \nPhone: '+ str(client.phone) + ' \nemail: ' + client.email + ' \nDescription: ' + client.details + '.'
    send_mail(
        'New Appointment',
        body,
        'siddservertest@gmail.com',
        ['siddharthbharmoria@gmail.com',],
        html_message= body1,
        fail_silently=False,   
    )