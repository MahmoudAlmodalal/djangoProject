from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book', views.book, name='book'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
]