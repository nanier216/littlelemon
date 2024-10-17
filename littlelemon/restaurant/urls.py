from django.urls import path
from .views import MenuItemsView, SingleMenuItemView, index # Import views from the current app

urlpatterns = [
    path('', index, name='index'),  # Route for the index view
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    
]
