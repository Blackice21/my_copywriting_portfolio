from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def landing_page(request):
    return render(request, 'landing_page.html')

def ps5_vs_switch(request):
    return render(request, 'switch_or_ps5.html')