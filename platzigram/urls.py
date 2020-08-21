"""Platzigram URLs Config"""

from django.urls import path

from platzigram import views as local_views
from posts import views as posts_views



urlpatterns = [
    path('hello/', local_views.hello), 
    path('sorted/', local_views.sorted),
    path('hi/<str:name>/<int:age>/', local_views.hi),

    path('posts/',posts_views.list_posts ),
]
