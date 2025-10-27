

# cart/urls.py
from django.urls import path
from .views import CartListCreateView, CartItemDetailView

urlpatterns = [
    path("", CartListCreateView.as_view(), name="cart-list-create"),
    path("<int:pk>/", CartItemDetailView.as_view(), name="cart-item-detail"),
]
