from rest_framework import serializers
from .models import Category, Item, Firm


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields = '__all__'

