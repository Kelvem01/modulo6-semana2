
from django.contrib import admin
from django.urls import path , include

from base.views import inicio , inscrever

urlpatterns = [
    path('',inicio,name='inicio'),
    path('inscrever-se/',inscrever,name='inscrever'),
    path('eventos/',include('eventos.urls', namespace='eventos')),
    path('api/',include('api.urls', namespace='api')),
    path('admin/', admin.site.urls),
]
