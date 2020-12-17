from django.urls import path
from .views import homePageView, addPageView, deletePageView

urlpatterns = [
    path('delete/<note_id>', deletePageView, name='delete'),
    path('add/', addPageView, name='add'),
    path('', homePageView, name='home')
]
