from django.contrib import admin
from django.urls import path
from clientes import views as cliente_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 ##   path('', cliente_views.home, name='home'),
 ##   path('cliente/add/', cliente_views.ClienteCreateView.as_view(), name="add_cliente"),
 
    path('add_cliente', cliente_views.home, name='home'),
    path('', cliente_views.ClienteCreateView.as_view(), name="add_cliente"),
 
    path('cliente/<int:pk>/', cliente_views.detalhes_cliente, name="detalhes_cliente"),
    path('cliente/<int:pk>/update/', cliente_views.ClienteUpdateView.as_view(), name="update_cliente"),
    path('cliente/<int:pk>/deleta/', cliente_views.deleta_cliente, name="deleta_cliente"),
    path('admin/', admin.site.urls),
]
 #  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
