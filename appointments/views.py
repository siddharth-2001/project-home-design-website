from django.shortcuts import render
from django.views import generic
from .models import Appointment, Quote
from django.http import HttpResponse
from .models import Appointment
from .logic import duplicate_checker
from django.core.mail import send_mail
from .mail import notify_email
from .forms import NewQuoteForm


# Create your views here.

def book_appointment_view(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    details = request.POST.get('info')
    if duplicate_checker(phone):
        notify_email(phone)
        return render(request, 'alrdy-success.html')
        
    else:
        Appointment.objects.create(name = name, phone = phone, email = email, details= details)
        notify_email(phone)
        return render(request, 'success.html')
       

def enter_details_view(request):
    return render(request,'appointment.html')

def get_quote_view(request):
    return render(request, 'get-quote.html')

def quote_details_view(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    prop_category = request.POST.get('propertyType')
    prop_type = request.POST.get('property')
    amt_rooms = request.POST.get('rooms[]')
    area      = request.POST.get('area')
    pincode   = request.POST.get('pincode')
    address   = request.POST.get('address')
    budget    = request.POST.get('budget')
    room_type = request.POST.getlist('roomType')
    Quote.objects.create(
        name = name,
        phone = phone,
        email = email,
        amt_rooms = amt_rooms,
        category = prop_category,
        property_type = prop_type,
        rooms = room_type,
        budget = budget,
        area = area,
        pincode = pincode,
        address = address
    )
    return render(request, 'success.html')