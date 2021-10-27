from django.shortcuts import render
from .models import Produit
# Create your views here.

def potoShop(request):
    if request.method == 'GET':
        produits = Produit.objects.all().order_by('-id')
        return render(request, 'shop/potoShop.html', {'produits':produits})      
