from django.shortcuts import render

# Create your views here.
from .models import Items

def item_list(request):
    items = Items.objects.all()
    return render(request, 'myEbag/item_list.html', {'items': items})

def item_detail(request, pk):
    items = Items.objects.get(id=pk)
    return render(request, 'myEbag/item_detail.html', {'items': items})