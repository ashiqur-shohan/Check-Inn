# from typing import Any
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Hotel
from booking.models import Booking
from booking.forms import BookingForm
from django.views.generic import DetailView
from review.forms import ReviewForm
from review.models import Review

# Create your views here.

def all_hotel(request,location_slug=None):
    hotel = Hotel.objects.all()
    if location_slug is not None:
        hotel = Hotel.objects.filter(location_slug = location_slug)
    # ekhane locations slug er unique value gula niye ashtesi. flate data data gulo ke ekta lista convert kore niye eshechi nahole list of tuple hoye ashbe
    locations  = Hotel.objects.values_list('location_slug',flat=True).distinct()
    context = {"data":hotel,"locations":locations}
    return render(request,'all_hotel.html',context)


def hotel_details(request,id):
    hotel = Hotel.objects.get(pk=id)
    review = Review.objects.filter(hotel=hotel)
    booking_check = None 
    if request.user.is_authenticated:      
        account = request.user.account
        booking_check = Booking.objects.filter(account=account,hotel=hotel).first()
        
    if request.method =="POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.account = request.user.account
            new_review.hotel = hotel
            new_review.save()
    else:
        review_form = ReviewForm()
    context = {'object' : hotel,"review_form":review_form,"booking_check":booking_check,'reviews':review}
    return render(request,'hotel_details.html',context)
    

def book_hotel(request,id):
    if request.method=="POST":
        date = request.POST.get('date')
        hotel_model = Hotel.objects.get(pk=id)
        user = request.user.account
        if user.balance > hotel_model.price:
            print("in logic")
            user.balance -= hotel_model.price
            user.save(update_fields=['balance'])
            Booking.objects.create(
                account = user,
                hotel = hotel_model,
                booking_date = date,
            )
        else:
            messages.error(request, 'You do not have sufficient balance')
            print("balance no")
            return redirect("hotel_details", id=id )
    return redirect("hotel_details", id=id )