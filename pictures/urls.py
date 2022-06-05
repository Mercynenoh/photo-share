from django.urls import path
from . import views


urlpatterns = [
  path('search/', views.search_results, name='search_results'),
  path('image/<str:pk>', views.viewPhoto, name='image'),
  path('followers_count/', views.followers_count, name='followers_count'),
]
