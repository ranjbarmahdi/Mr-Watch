from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.product_list, name="product_list"),
    path('detail/<int:id>', views.product_detail, name="product_detail"),
    path('detail/<int:id>/comment', views.product_detail, name="product_detail_comment"),
    path('contact/', views.ticket, name="ticket")
]