# from rest_framework import serializers
# from .models import Items

# class ItemSerializer(serializers.HyperlinkedModelSerializer):
#     items = serializers.HyperlinkedRelatedField(
#         view_name='item_detail',
#         many=True,
#         read_only=True
#     )
#     class Meta:
#         model = Items
#         fields = ("id", "name", "description", "photo_url", "items")