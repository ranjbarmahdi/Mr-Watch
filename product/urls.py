from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'product'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.product_list, name="product_list"),
    path('detail/<int:id>', views.product_detail, name="product_detail"),
    path('detail/<int:id>/comment', views.product_comment, name="product_detail_comment"),
    path('contact/', views.ticket, name="ticket"),
    path('serach/', views.product_search, name='product_search'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
