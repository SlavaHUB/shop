from django.shortcuts import render
from .models import Product
# Create your views here.

def catalog(request):
    product = Product.objects.all()    
    return render(request, 'catalog.html', {'product': product})