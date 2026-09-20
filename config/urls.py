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
from django.urls import (  # Aula 19: Adicionado 'include' para incluir rotas de outros apps
    include,
    path,
)
from drf_spectacular.views import (  # Aula 20: Importação das views do drf-spectacular para documentação
    SpectacularAPIView,  # Aula 20: View que gera o esquema OpenAPI no formato YAML/JSON
    SpectacularRedocView,  # Aula 20: View da interface de documentação ReDoc
    SpectacularSwaggerView,  # Aula 20: View da interface interativa Swagger UI
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # --- ROTAS DA API ---
    path('api/', include('produtos.urls')),  # Aula 19: Redireciona requisições de /api/ para produtos.urls
    # --- DOCUMENTAÇÃO DA API (AULA 20) ---
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # Aula 20: Endpoint do esquema OpenAPI bruto
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Aula 20: Endpoint da interface Swagger UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # Aula 20: Endpoint da interface ReDoc
]