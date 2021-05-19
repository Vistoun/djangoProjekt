# Import modulu path z balíku django.urls
from django.urls import path
# Import modulu views (soubor views.py) ze stejné složky (.)
from . import views
# URL mapování -seznam URL adres pro aplikaci 
urlpatterns = [
    path('', views.index, name='index'),
    path('opravy/<int:pk>/', views.ModelDetailView.as_view(), name='model-detail'),
    path('opravy/', views.OpravarAbout.as_view(), name='opravar_about'),
    path('opravy/', views.ModelListView.as_view(), name='model-brand'),
]