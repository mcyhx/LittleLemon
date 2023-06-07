from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer,MenuItemSerializer,BookingSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import MenuItem,Booking

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

@permission_classes([IsAuthenticated])		
class MenuItemsView(generics.ListCreateAPIView):
	queryset = MenuItem.objects.all()
	serializer_class = MenuItemSerializer

@permission_classes([IsAuthenticated])	
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	queryset = MenuItem.objects.all()
	serializer_class = MenuItemSerializer

@permission_classes([IsAuthenticated])	
class BookingListCreateView(generics.ListCreateAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer

@permission_classes([IsAuthenticated])	
class SingleBookingview(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer

