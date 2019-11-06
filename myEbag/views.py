from django.shortcuts import render

# Create your views here.
from .models import Items

def item_list(request):
    items = Items.objects.all()
    return render(request, 'Ebag/item_list.html', {'items': items})