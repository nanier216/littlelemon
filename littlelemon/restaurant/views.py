from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework import viewsets, permissions


# Create your views here.
def index(request):
 return render(request, 'index.html', {})

# Handles GET (list) and POST (create) requests
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Handles GET (retrieve), PUT (update), and DELETE requests
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Fetch all Booking objects
    serializer_class = BookingSerializer  # Use BookingSerializer for this viewset
    permission_classes = [permissions.IsAuthenticated] 