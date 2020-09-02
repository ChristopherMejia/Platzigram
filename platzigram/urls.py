"""Platzigram URLs Config"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from platzigram import views as local_views
from posts import views as posts_views



urlpatterns = [

    path('admin/', admin.site.urls),

    path('hello/', local_views.hello), 
    path('sorted/', local_views.sorted),
    path('hi/<str:name>/<int:age>/', local_views.hi),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
