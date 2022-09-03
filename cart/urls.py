from django.urls import path, include
from .views import cart_detail_view


urlpatterns = [
    path('', cart_detail_view, name='cart_detail'),
]
