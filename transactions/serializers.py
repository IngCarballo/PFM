from rest_framework import serializers
from .models import Movement, Category

class MovementSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Movement
        fields = [
            'id',
            'user',
            'amount',
            'description',
            'payment_method',
            'link',
            'icon',
            'date',
            'category',
        ]
        extra_kwargs = {
            'user': {'read_only': True},
            'date': {'read_only': True},  # Opcional, si tu modelo usa auto_now_add
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
