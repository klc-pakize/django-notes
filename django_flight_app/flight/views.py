from django.shortcuts import render

from datetime import date, datetime

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions


from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer, StaffReservationSerializers
from .models import Flight, Passenger, Reservation
from .permissions import IsStaffOrReadOnly
# Create your views here.

class FlightView(ModelViewSet):

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStaffOrReadOnly,)

    def get_serializer_class(self):
        serializer = super().get_serializer_class()

        if self.request.user.is_staff:
            return StaffReservationSerializers

        return serializer


#! We have customed the get_queryset method so that users can only view the future flight

    def get_queryset(self):

        now = datetime.now()  # Gets the current time
        current_time = now.strftime('%H:%M:%S')   # Gets the current time in hours and minutes
        today = date.today()  # Gets today's date

        if self.request.user.is_staff:
            return super().get_queryset()

        else:
            queryset = Flight.objects.filter(date_of_departure__gt = today)

            if Flight.objects.filter(date_of_departure = today):

                today_qs = Flight.objects.filter(etd__gt = current_time)
                queryset = queryset.union(today_qs)  # Union is used to join 2 querysets
            
            return queryset


class ReservationView(ModelViewSet):
    
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):

        queryset = super().get_queryset()  # super() = represents parent | super().get_queryset() = Reservation.objects.all()

        if self.request.user.is_staff:  # This is how we can get the id of the requesting user | If user staff, display all querysets
            return queryset
        return queryset.filter(user = self.request.user)  # If the user is not staff, only display their own queryset

        """
        Get the list of items for this view.
        This must be an iterable, and may be a queryset.
        Defaults to using `self.queryset`.

        This method should always be used rather than accessing `self.queryset`
        directly, as `self.queryset` gets evaluated only once, and those results
        are cached for all subsequent requests.

        You may want to override this if you need to provide different
        querysets depending on the incoming request.

        (Eg. return a list of items that is specific to the user)
        """