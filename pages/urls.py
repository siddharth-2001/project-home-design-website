from django.urls import path
from .views import home_view, terms_view, about_view


urlpatterns = [
    path('', home_view, name = 'home'),
    path('terms', terms_view, name = 'terms'),
    path('about', about_view, name = 'about'),
]