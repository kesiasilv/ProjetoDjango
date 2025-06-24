from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Agora tudo que for '', 'add/', 'edit/22/', etc, vem de tasks.urls
]