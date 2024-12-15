from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('api/', include('api.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicons/favicon.ico', permanent=True)),
]
