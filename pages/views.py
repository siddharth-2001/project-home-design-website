from django.shortcuts import render
from django.views.decorators.http import require_GET

# Create your views here.
@require_GET
def home_view(request):
    return render(request, 'home.html')
@require_GET
def terms_view(request):
    return render(request, 'terms.html')
@require_GET
def about_view(request):
    return render(request, 'about.html')