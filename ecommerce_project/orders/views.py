# orders/views.py
from rest_framework import generics, permissions
from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import CartItem
from products.models import Product
from rest_framework.response import Response
from django.db import transaction

class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        user = request.user
        cart_items = CartItem.objects.filter(user=user).select_related("product")
        if not cart_items.exists():
            return Response({"detail": "Cart is empty."}, status=400)

        total = 0
        for ci in cart_items:
            if ci.quantity > ci.product.stock:
                return Response({"detail": f"Not enough stock for {ci.product.name}"}, status=400)
            total += ci.product.price * ci.quantity

        # create order
        order = Order.objects.create(user=user, total_amount=total, status="PENDING")
        # create order items and reduce stock
        for ci in cart_items:
            OrderItem.objects.create(
                order=order,
                product=ci.product,
                quantity=ci.quantity,
                price_at_purchase=ci.product.price,
            )
            # reduce stock
            ci.product.stock -= ci.quantity
            ci.product.save()
        # clear cart
        cart_items.delete()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=201)

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all().order_by("-created_at")
        return Order.objects.filter(user=user).order_by("-created_at")

class OrderDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)
