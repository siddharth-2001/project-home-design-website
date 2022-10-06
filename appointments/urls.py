from django.urls import path
from .views import book_appointment_view, enter_details_view, get_quote_view, quote_details_view

urlpatterns = [
    path('book-appointment', enter_details_view, name = 'book-app'),
    path('book-appointment/success', book_appointment_view, name = 'app-success'),
    path('get-quote', get_quote_view, name = 'get-quote'),
    path('get-quote-success', quote_details_view, name = 'quote-success'),

]