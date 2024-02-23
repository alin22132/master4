from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('/<str:category_name>/', views.category_detail, name='category_detail'),
    path('/<str:category_name>/<str:brand_name>/models/', views.model_list, name='model_list'),
    path('/<str:category_name>/<str:brand_name>/<str:model_name>/items/', views.items, name='items'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
