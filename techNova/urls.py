from django.contrib import admin
from django.urls import path, include  # Importando 'include' para incluir as urls do app 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Aqui o Django procura o arquivo 'urls.py' dentro do app 'core'
]
