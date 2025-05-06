from rest_framework import serializers
from .models import Movement, Category
from django.db.models import Q

class MovementSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.none())

    class Meta:
        model = Movement
        fields = [
            'id', 'user', 'amount', 'description', 'payment_method',
            'link', 'icon', 'date', 'category',
        ]
        extra_kwargs = {
            'user': {'read_only': True},
            'date': {'read_only': True},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        self.fields['category'].queryset = Category.objects.filter(
            Q(user=user) | Q(user__isnull=True)
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }
