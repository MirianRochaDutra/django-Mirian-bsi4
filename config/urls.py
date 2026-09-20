"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import (  # Aula 19: Adicionado 'include' para incluir rotas
    include,
    path,
)
from drf_spectacular.views import (  # Aula 21: Importação das views do drf-spectacular para documentação
    SpectacularAPIView,  # Aula 21: View que gera o esquema OpenAPI no formato YAML/JSON
    SpectacularRedocView,  # Aula 21: View da interface de documentação ReDoc
    SpectacularSwaggerView,  # Aula 21: View da interface interativa Swagger UI
)
from rest_framework.routers import (
    DefaultRouter,  # Aula 21: Importação do DefaultRouter do DRF
)

from produtos.views import ProdutoViewSet  # Aula 21: Importação da ViewSet de Produtos

# --- REGISTRO DO ROTEADOR DRF (AULA 21) ---
router = DefaultRouter()  # Aula 21: Criação da instância do roteador padrão
router.register(r'produtos', ProdutoViewSet, basename='produto')  # Aula 21: Registro das rotas /api/produtos/

urlpatterns = [
    path('admin/', admin.site.urls),
    # --- ROTAS DA API (AULA 21) ---
    path('api/', include(router.urls)),  # Aula 21: Inclui as rotas do router na raiz /api/
    # --- DOCUMENTAÇÃO DA API (AULA 21) ---
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # Aula 21: Endpoint do esquema OpenAPI bruto
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Aula 21: Endpoint da interface Swagger UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # Aula 21: Endpoint da interface ReDoc
]