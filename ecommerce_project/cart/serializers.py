# cart/serializers.py
from rest_framework import serializers
from .models import CartItem
from products.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=None, source="product")

    class Meta:
        model = CartItem
        fields = ("id", "product", "product_id", "quantity", "added_at")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set queryset dynamically to avoid circular import at import time
        from products.models import Product
        self.fields["product_id"].queryset = Product.objects.all()

    def create(self, validated_data):
        user = self.context["request"].user
        product = validated_data["product"]
        quantity = validated_data.get("quantity", 1)
        obj, created = CartItem.objects.get_or_create(user=user, product=product, defaults={"quantity": quantity})
        if not created:
            obj.quantity += quantity
            obj.save()
        return obj
