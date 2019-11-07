from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/<int:pk>', views.item_detail, name='item_detail'),
    path('item/<int:pk>/edit', views.item_edit, name='item_edit'),
    path('item/new', views.item_create, name="item_create"),
    path('item/<int:pk>delete', views.item_delete, name="item_delete")
    # path('items/', views.ItemList.as_view(), name='artist_list'),
    # path('items/<int:pk>', views.ItemDetail.as_view(), name="item_detail")


]