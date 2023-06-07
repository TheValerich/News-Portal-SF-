from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('accounts.urls')),
    path('', include('protect.urls')),
    path('articles/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('sign/', include('sign.urls')),
]
