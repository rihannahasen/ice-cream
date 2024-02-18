from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home .html')
 
def about(request):
    return HttpResponse('about page')

def contact_us(request):
    return HttpResponse('contact_us page')

def product(request):
    return HttpResponse('product page ')
