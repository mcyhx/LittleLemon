from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('', views.index, name='index'),
    path('menuitems/', views.MenuItemsView.as_view(), name='menuitems-list'),
    path('menuitems/<int:pk>/', views.SingleMenuItemView.as_view(), name='menuitems-detail'),
    path("bookings/",views.BookingListCreateView.as_view(), name="bookings"),
    path('bookings/<int:pk>/', views.SingleBookingview.as_view(), name='booking-detail'),
    path('api-token-auth/', obtain_auth_token),
]