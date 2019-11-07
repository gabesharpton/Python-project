from django.shortcuts import render, redirect

# # Create your views here.
from .models import Items
from .forms import ItemForm

# from rest_framework import generics
# from .serializers import ItemSerializer

# class ItemList(generics.ListCreateAPIView):
#     queryset = Items.objects.all()
#     serializer_class = ItemSerializer

# class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Items.objects.all()
#     serializer_class = ItemSerializer



def item_list(request):
    items = Items.objects.all()
    return render(request, 'myEbag/item_list.html', {'items': items})

def item_detail(request, pk):
    items = Items.objects.get(id=pk)
    return render(request, 'myEbag/item_detail.html', {'items': items})

def item_edit(request, pk):
    items = Items.objects.get(pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=items)
        if form.is_valid():
            items = form.save()
            return redirect('item_detail', pk=items.pk)
    else:
        form = ItemForm(instance=items)
    return render(request, 'myEbag/item_form.html', {'form': form})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            items = form.save()
            return redirect('item_detail', pk=items.pk)
    else:
        form = ItemForm()
        return render(request, 'myEbag/item_form.html', {'form': form})

def item_delete(request, pk):
    Items.objects.get(id=pk).delete()
    return redirect('item_list')