from django.urls import path
from .views import all_hotel,book_hotel,hotel_details
urlpatterns = [
    path('hotel_details/<int:id>/',hotel_details,name='hotel_details'),
    path('book/<int:id>/',book_hotel,name='book'),
    path('all_hotel/',all_hotel,name='all_hotel'),
    path('all_hotel/<slug:location_slug>/',all_hotel,name='location_wise_hotel'),
]